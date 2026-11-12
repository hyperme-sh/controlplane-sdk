"""Capture urllib3 multipart encoding without opening a network connection."""
import json
from pathlib import Path

import pytest
from pydantic import ValidationError
from openapi_client import ApiClient, Configuration
from openapi_client.api.branding_api import BrandingApi
from openapi_client.api.users_api import UsersApi
from spanopticon_sdk_gen.rest_codegen import sanitize_openapi_for_generator


class Captured(Exception):
    pass


def operation(client, kind):
    if kind == 'logo':
        return BrandingApi(client).upload_logo_api_v1_brandings_logo_put, {}
    return UsersApi(client).update_profile_picture_api_v1_users_user_id_update_profile_picture_put, {'user_id': 'test-user'}


@pytest.mark.parametrize('kind', ['logo', 'avatar'])
@pytest.mark.parametrize('input_kind', ['path', 'bytes', 'named_bytes'])
def test_upload_sends_binary_multipart(monkeypatch, tmp_path, kind, input_kind):
    payload = b'\x89PNG\r\n\x1a\n\x00\xffbinary-image'
    path = tmp_path / 'picture.png'
    path.write_bytes(payload)
    value = {'path': str(path), 'bytes': payload, 'named_bytes': ('picture.png', payload)}[input_kind]
    captured = {}
    with ApiClient(Configuration(host='https://unit.invalid')) as client:
        def capture(method, url, **kwargs):
            captured.update(method=method, url=url, **kwargs)
            raise Captured
        monkeypatch.setattr(client.rest_client.pool_manager, 'urlopen', capture)
        call, kwargs = operation(client, kind)
        with pytest.raises(Captured):
            call(file=value, **kwargs)
    assert captured['method'] == 'PUT'
    assert captured['headers']['Content-Type'].startswith('multipart/form-data; boundary=')
    assert payload in captured['body']
    filename, mime = ('file', 'application/octet-stream') if input_kind == 'bytes' else ('picture.png', 'image/png')
    assert f'name="file"; filename="{filename}"'.encode() in captured['body']
    assert f'Content-Type: {mime}'.encode() in captured['body']
    assert str(path).encode() not in captured['body']


@pytest.mark.parametrize('kind', ['logo', 'avatar'])
@pytest.mark.parametrize('value', [42, {'file': b'data'}, ('picture.png', 42), None])
def test_upload_rejects_invalid_values(kind, value):
    with ApiClient(Configuration(host='https://unit.invalid')) as client:
        call, kwargs = operation(client, kind)
        with pytest.raises(ValidationError):
            call(file=value, **kwargs)


def test_upload_missing_path_has_clear_error(tmp_path):
    with ApiClient(Configuration(host='https://unit.invalid')) as client:
        call, kwargs = operation(client, 'logo')
        with pytest.raises(FileNotFoundError):
            call(file=str(tmp_path/'missing.png'), **kwargs)


def test_generator_normalizes_only_multipart_copy():
    document = json.loads((Path(__file__).resolve().parents[1]/'sdk/openapi/v1/openapi.json').read_text())
    original = json.dumps(document, sort_keys=True)
    result = sanitize_openapi_for_generator(document)
    content = result['paths']['/api/v1/brandings/logo']['put']['requestBody']['content']
    assert content['multipart/form-data']['schema']['properties']['file']['format'] == 'binary'
    assert 'format' not in result['components']['schemas']['Body_upload_logo_api_v1_brandings_logo_put']['properties']['file']
    assert json.dumps(document, sort_keys=True) == original
