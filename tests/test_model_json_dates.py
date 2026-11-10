"""Generated JSON helpers must agree with model parsing and request wire dates."""
from datetime import date, datetime, timedelta, timezone
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest
from openapi_client import ApiClient, Configuration
from openapi_client.models.inference_record_response import InferenceRecordResponse
from openapi_client.models.registered_passkey_credentials_dto import RegisteredPasskeyCredentialsDto
from openapi_client.models.user_response import UserResponse

STAMP = datetime(2026, 3, 4, 5, 6, 7, 123456, tzinfo=timezone(timedelta(hours=5, minutes=45)))

def user(**overrides):
    return UserResponse(id='unit-user',tenant_id='unit-tenant',email='unit@example.invalid',
                        first_name='Unit',last_name='Test',gender='other',is_active=True,**overrides)

@pytest.mark.parametrize('model,field',[
    (user(deleted_at=STAMP),'deleted_at'),
    (InferenceRecordResponse(id='unit-record',created_at=STAMP,user_id='unit-user',model='unit-model',input_tokens=1,output_tokens=2,cost_usd='0',billing_mode='none'),'created_at'),
    (RegisteredPasskeyCredentialsDto(credential_id='unit-credential',public_key='unit-public-key',sigin_count=0,created_at=STAMP,last_used_at=STAMP),'created_at'),
])
def test_all_timestamp_models_roundtrip_aware_datetimes(model,field):
    encoded=model.to_json()
    assert json.loads(encoded)[field]==STAMP.isoformat()
    restored=type(model).from_json(encoded)
    assert getattr(restored,field)==STAMP
    assert json.loads(restored.to_json())==json.loads(encoded)

def test_nested_dates_and_existing_null_omission_semantics():
    model=user(sociacl_attributes={'on':date(2026,3,4),'nested':[{'at':STAMP,'keep_null':None}]})
    encoded=json.loads(model.to_json())
    assert encoded['sociacl_attributes']=={'on':'2026-03-04','nested':[{'at':STAMP.isoformat(),'keep_null':None}]}
    assert 'deleted_at' not in encoded
    assert model.to_dict()['sociacl_attributes']['on']==date(2026,3,4)
    assert json.loads(UserResponse.from_json(json.dumps(encoded)).to_json())==encoded

def test_unrelated_non_json_objects_still_fail_clearly():
    with pytest.raises(TypeError,match='not JSON serializable'):
        user(sociacl_attributes={'unsupported':object()}).to_json()

def test_model_json_matches_actual_request_serialization():
    model=user(deleted_at=STAMP,sociacl_attributes={'on':date(2026,3,4)})
    captured=[]
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            captured.append(json.loads(self.rfile.read(int(self.headers['Content-Length']))))
            self.send_response(200);self.send_header('Content-Length','0');self.end_headers()
        def log_message(self,*args):pass
    with ThreadingHTTPServer(('127.0.0.1',0),Handler) as server:
        worker=threading.Thread(target=server.serve_forever,daemon=True);worker.start()
        try:
            with ApiClient(Configuration(host=f'http://127.0.0.1:{server.server_port}')) as client:
                params=client.param_serialize('POST','/unit-date',header_params={'Content-Type':'application/json'},body=model)
                response=client.call_api(*params,_request_timeout=5)
                assert response.status==200
        finally:
            server.shutdown();worker.join(timeout=5)
    assert captured==[json.loads(model.to_json())]
