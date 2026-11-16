"""Auth example wire contracts, with all HTTP mocked."""
import importlib.util
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import httpx
import pytest
import respx

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sdk_auth_example', ROOT / 'sdk/auth/python/keycloak_auth.py')
auth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auth)


def test_pkce_vector_and_authorization_parameters():
    verifier = 'dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk'
    assert auth.pkce_challenge_s256(verifier) == 'E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM'
    assert 43 <= len(auth.pkce_verifier()) <= 128
    url = auth.build_authorize_url(authorization_endpoint='https://id.example/auth',
        client_id='public',redirect_uri='https://app.example/callback?a=1',state='s + &',code_challenge='challenge')
    query = parse_qs(urlsplit(url).query)
    assert query['state'] == ['s + &']
    assert query['code_challenge_method'] == ['S256']
    assert query['redirect_uri'] == ['https://app.example/callback?a=1']
    assert auth.api_key_headers(api_key='key',tenant_id='tenant') == {'X-Api-Key':'key','X-Tenant-ID':'tenant'}


@pytest.mark.asyncio
async def test_auth_grants_and_owner_failures():
    endpoint = 'https://id.example/token'
    with respx.mock(assert_all_called=False) as router:
        route = router.post(endpoint).mock(return_value=httpx.Response(200,json={'access_token':'unit-token'}))
        assert (await auth.exchange_code_for_tokens(token_endpoint=endpoint,client_id='public',redirect_uri='https://app.example/cb',code='code+',code_verifier='verifier'))['access_token']=='unit-token'
        fields = parse_qs(route.calls[-1].request.content.decode())
        assert fields['grant_type']==['authorization_code'] and fields['code']==['code+']
        assert fields['code_verifier']==['verifier'] and 'client_secret' not in fields
        await auth.client_credentials_token(token_endpoint=endpoint,client_id='server',client_secret='unit-secret')
        assert parse_qs(route.calls[-1].request.content.decode())['grant_type']==['client_credentials']
        await auth.start_device_code_flow(device_endpoint=endpoint,client_id='public')
        assert 'client_secret' not in parse_qs(route.calls[-1].request.content.decode())
        await auth.poll_device_token(token_endpoint=endpoint,client_id='public',device_code='device')
        assert parse_qs(route.calls[-1].request.content.decode())['grant_type']==['urn:ietf:params:oauth:grant-type:device_code']
        for status,error in [(400,'authorization_pending'),(400,'slow_down'),(403,'access_denied'),(503,'unavailable')]:
            route.mock(return_value=httpx.Response(status,json={'error':error}))
            with pytest.raises(httpx.HTTPStatusError):
                await auth.poll_device_token(token_endpoint=endpoint,client_id='public',device_code='device')
        discovery = router.get('https://id.example/realms/controlplane/.well-known/openid-configuration').mock(return_value=httpx.Response(200,json={'token_endpoint':endpoint}))
        assert (await auth.fetch_well_known('https://id.example/','controlplane'))['token_endpoint']==endpoint
        assert discovery.called
