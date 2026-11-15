"""Wallet owner snapshots and generated wire contracts remain provider-free."""
import json
from pathlib import Path
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest


def test_owner_snapshot_parity():
    root = Path(__file__).resolve().parents[1] / 'sdk/openapi'
    merged = json.loads((root / 'v1/openapi.json').read_text())
    for name in ('auth-wallet', 'payment-wallet'):
        owner = json.loads((root / f'owners/{name}.json').read_text())
        for path, operations in owner['paths'].items():
            assert merged['paths'][path] == operations
        for name, schema in owner['components']['schemas'].items():
            assert merged['components']['schemas'][name] == schema
    assert 'stripe' not in json.dumps(merged).lower()


@pytest.fixture
def wire():
    calls = []
    replies = []
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self): self.reply()
        def do_POST(self): self.reply()
        def reply(self):
            calls.append((self.command, self.path, dict(self.headers), self.rfile.read(int(self.headers.get('Content-Length',0)))))
            status, body = replies.pop(0)
            encoded = json.dumps(body).encode()
            self.send_response(status)
            self.send_header('Content-Type','application/json')
            self.send_header('Content-Length',str(len(encoded)))
            self.end_headers(); self.wfile.write(encoded)
        def log_message(self,*args): pass
    server=HTTPServer(('127.0.0.1',0),Handler)
    worker=threading.Thread(target=server.serve_forever,daemon=True);worker.start()
    try: yield f'http://127.0.0.1:{server.server_port}',calls,replies
    finally: server.shutdown();worker.join();server.server_close()


def client(url):
    from openapi_client import ApiClient, Configuration
    config=Configuration(host=url,access_token='scoped-session')
    result=ApiClient(config)
    result.set_default_header('X-Tenant-ID','11111111-1111-4111-8111-111111111111')
    return result


def test_disabled_capability_is_observation_without_payment(wire):
    from openapi_client.api.wallet_payments_api import WalletPaymentsApi
    url,calls,replies=wire
    replies.append((200,dict(contract_version='wallet-payments/v1',mode='sandbox',production_payments=False,
        checkout_creation=False,deposit_creation=False,payout_address_proof=False,usdc_host_enrollment=False,
        deposit_observation=True,refund_recovery='owner_managed',settlement_authority='verified_provider_confirmation',
        accounting_effect='confirmed_capacity_only',enterprise_units_redeemable=False)))
    with client(url) as transport:
        result=WalletPaymentsApi(transport).get_wallet_payment_capabilities('11111111-1111-4111-8111-111111111111')
    assert result.deposit_creation is False and result.enterprise_units_redeemable is False
    assert len(calls)==1 and calls[0][:2]==('GET','/api/v1/payments/wallet/capabilities')
    assert calls[0][2]['Authorization']=='Bearer scoped-session'
    assert calls[0][2]['X-Tenant-ID']=='11111111-1111-4111-8111-111111111111'


@pytest.mark.parametrize('status',[400,403,404,409,503])
def test_owner_refusals_remain_errors_not_paid_results(wire,status):
    from openapi_client.api.wallet_payments_api import WalletPaymentsApi
    from openapi_client.exceptions import ApiException
    url,calls,replies=wire
    replies.append((status,{'detail':'owner refused'}))
    with client(url) as transport, pytest.raises(ApiException) as exc:
        WalletPaymentsApi(transport).get_wallet_deposit('22222222-2222-4222-8222-222222222222','11111111-1111-4111-8111-111111111111')
    assert exc.value.status==status
    assert len(calls)==1


def test_wallet_binding_preserves_server_message_and_signature(wire):
    from openapi_client.api.wallet_auth_api import WalletAuthApi
    from openapi_client.models.wallet_auth_siwe_bind_request import WalletAuthSiweBindRequest
    url,calls,replies=wire
    replies.append((200,dict(keycloak_sub='person',wallet_address='0x'+'11'*20,bound=True)))
    with client(url) as transport:
        api=WalletAuthApi(transport)
        api.auth_siwe_bind_auth_siwe_bind_post(WalletAuthSiweBindRequest(message='owner-issued message',signature='0x1234'))
    assert calls[0][:2]==('POST','/auth/siwe/bind')
    assert json.loads(calls[0][3])=={'message':'owner-issued message','signature':'0x1234'}
