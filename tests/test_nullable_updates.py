"""Request serialization contracts; no network or server required."""
import importlib
import json
from pathlib import Path

import pytest
from openapi_client import ApiClient, Configuration
from openapi_client.models.listing_update_body import ListingUpdateBody
from spanopticon_sdk_gen.nullable_updates import install_nullable_updates

CASES = [
    ('listing_update_body', 'ListingUpdateBody', 'description', {}),
    ('user_update_body', 'UserUpdateBody', 'first_name', {}),
    ('update_branding_dto', 'UpdateBrandingDto', 'identity', {}),
    ('update_role_dto', 'UpdateRoleDto', 'description', {'name':'reader','permissions':[]}),
    ('update_sso_settings_dto', 'UpdateSSOSettingsDto', 'client_secret', {}),
    ('update_tenant_dto', 'UpdateTenantDto', 'custom_domain', {}),
]


@pytest.mark.parametrize('module,name,field,base', CASES)
def test_nullable_updates_distinguish_omitted_and_explicit_null(module, name, field, base):
    cls = getattr(importlib.import_module('openapi_client.models.'+module), name)
    with ApiClient(Configuration(host='https://unit.invalid')) as client:
        def body(model):
            return client.param_serialize('PATCH', '/unit', body=model)[3]
        assert field not in body(cls(**base))
        assert body(cls(**base, **{field:None}))[field] is None
        assert field not in body(cls.from_dict(base))
        assert body(cls.from_dict({**base,field:None}))[field] is None
        assert field not in body(cls.from_json(json.dumps(base)))


def test_non_null_values_and_assignment_are_preserved():
    model = ListingUpdateBody(description='keep', is_public=False, metadata={'nested':None})
    assert model.to_dict() == {'description':'keep','is_public':False,'metadata':{'nested':None}}
    model.description = None
    assert model.to_dict()['description'] is None
    assert 'title' not in model.to_dict()


def test_generator_reinstalls_nullable_handling_idempotently(tmp_path):
    source = Path(__file__).resolve().parents[1]/'sdk/rest/python/openapi_client/models/listing_update_body.py'
    target = tmp_path/'openapi_client/models/listing_update_body.py'
    target.parent.mkdir(parents=True)
    text = source.read_text()
    text = '\n'.join(line for line in text.split('\n') if not line.startswith('from openapi_client._nullable_updates'))
    text = text.replace("return with_explicit_nulls(self, _dict, ('title', 'description', 'metadata', 'is_public'))", 'return _dict')
    text = text.replace('return restore_fields_set(_obj, obj)', 'return _obj')
    target.write_text(text)
    document = json.loads((source.parents[4]/'openapi/v1/openapi.json').read_text())
    document['components']['schemas'] = {'ListingUpdateBody': document['components']['schemas']['ListingUpdateBody']}
    install_nullable_updates(tmp_path, document)
    first = target.read_text()
    install_nullable_updates(tmp_path, document)
    assert target.read_text() == first
    assert 'return with_explicit_nulls(' in first
    assert 'return restore_fields_set(' in first
