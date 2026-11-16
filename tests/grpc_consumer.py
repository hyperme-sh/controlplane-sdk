"""Socket-free consumer contracts for one protobuf import layout per process."""
import importlib
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root))
prefix = '' if (root / 'contractecho_pb2.py').exists() else 'spanopticon.v1.'
pb = importlib.import_module(prefix + 'contractecho_pb2')
api = importlib.import_module(prefix + 'contractecho_pb2_grpc')

class Channel:
    def __init__(self):
        self.methods = []
    def unary_unary(self, name, request_serializer, response_deserializer, **kwargs):
        self.methods.append(name)
        def echo(value):
            wire = request_serializer(value)
            assert isinstance(wire, bytes)
            return response_deserializer(wire)
        return echo

channel = Channel()
stub = api.ContractEchoStub(channel)
listing = pb.ListingWire(id='listing', tenant_id='tenant', price_amount=0, sku='')
assert listing.HasField('price_amount') and listing.HasField('sku')
assert stub.EchoListing(listing) == listing
missing = stub.EchoListing(pb.ListingWire(id='other'))
assert not missing.HasField('price_amount') and not missing.HasField('sku')
usage = pb.TokenUsageWire(user_id='user', tenant_id='tenant', model='model',
                         input_tokens=123, output_tokens=456, cost_usd='0.000012345')
usage.timestamp.seconds = 1700000000
usage.timestamp.nanos = 123456789
assert stub.EchoTokenUsage(usage) == usage
user = pb.UserWire(id='user', display_name='Zoë', tenant_id='tenant')
assert stub.EchoUser(user) == user
assert not stub.EchoUser(pb.UserWire(id='other')).HasField('tenant_id')
assert channel.methods == ['/spanopticon.v1.ContractEcho/' + x for x in
                           ('EchoListing', 'EchoTokenUsage', 'EchoUser')]
assert pb.ListingWire.DESCRIPTOR.fields_by_name['price_amount'].number == 8
assert pb.UserWire.DESCRIPTOR.fields_by_name['tenant_id'].number == 4
print('gRPC serializers, method paths, optional presence and timestamp precision passed')
