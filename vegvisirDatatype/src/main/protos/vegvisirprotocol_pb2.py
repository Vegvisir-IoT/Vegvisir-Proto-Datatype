# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vegvisirprotocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from overhaul.protos import charlottewrapper_pb2 as overhaul_dot_protos_dot_charlottewrapper__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vegvisirprotocol.proto',
  package='overhaul.protos',
  syntax='proto3',
  serialized_pb=_b('\n\x16vegvisirprotocol.proto\x12\x0foverhaul.protos\x1a&overhaul/protos/charlottewrapper.proto\"\x19\n\tBlockHash\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\"9\n\rVegvisirBlock\x12(\n\x08vegblock\x18\x01 \x01(\x0b\x32\x16.overhaul.protos.Block\"\xb0\x03\n\x0bPeerRequest\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.overhaul.protos.PeerRequest.RequestType\x12\x31\n\rtarget_hashes\x18\x02 \x03(\x0b\x32\x1a.overhaul.protos.BlockHash\x12\x35\n\rblocks_to_add\x18\x03 \x03(\x0b\x32\x1e.overhaul.protos.VegvisirBlock\"\xfe\x01\n\x0bRequestType\x12\x11\n\rDUMMY_REQUEST\x10\x00\x12\x15\n\x11SEND_FRONTIER_SET\x10\x01\x12\x11\n\rSEND_BCHASHES\x10\x02\x12\x0e\n\nSEND_BLOCK\x10\x03\x12\r\n\tADD_BLOCK\x10\x04\x12\x0e\n\nCREATE_POW\x10\x05\x12\x19\n\x15SEND_REQUEST_SET_SIZE\x10\x06\x12\x1e\n\x1aSELF_RECONCILIATION_NEEDED\x10\x07\x12\x1e\n\x1aPEER_RECONCILIATION_NEEDED\x10\x08\x12\x16\n\x12READY_FOR_PROTOCOL\x10\t\x12\x10\n\x0c\x45ND_PROTOCOL\x10\n\"?\n\x0b\x46rontierSet\x12\x30\n\x0c\x62lock_hashes\x18\x01 \x03(\x0b\x32\x1a.overhaul.protos.BlockHash\"D\n\x14SendBlockchainHashes\x12,\n\x08hash_set\x18\x01 \x03(\x0b\x32\x1a.overhaul.protos.BlockHash\";\n\tSendBlock\x12.\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x1e.overhaul.protos.VegvisirBlock\"9\n\x08\x41\x64\x64\x42lock\x12-\n\x05\x62lock\x18\x01 \x03(\x0b\x32\x1e.overhaul.protos.VegvisirBlock\"#\n\x0eRequestSetSize\x12\x11\n\trset_size\x18\x0b \x01(\x05\"\xd4\x02\n\x0cPeerResponse\x12=\n\x15\x66rontier_set_response\x18\x01 \x01(\x0b\x32\x1c.overhaul.protos.FrontierSetH\x00\x12\x43\n\x12\x62\x63_hashes_response\x18\x02 \x01(\x0b\x32%.overhaul.protos.SendBlockchainHashesH\x00\x12\x39\n\x13send_block_response\x18\x03 \x01(\x0b\x32\x1a.overhaul.protos.SendBlockH\x00\x12.\n\tadd_block\x18\x04 \x01(\x0b\x32\x19.overhaul.protos.AddBlockH\x00\x12>\n\x13r_set_size_response\x18\x06 \x01(\x0b\x32\x1f.overhaul.protos.RequestSetSizeH\x00\x42\x15\n\x13peer_response_typesb\x06proto3')
  ,
  dependencies=[overhaul_dot_protos_dot_charlottewrapper__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PEERREQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='overhaul.protos.PeerRequest.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DUMMY_REQUEST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_FRONTIER_SET', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_BCHASHES', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_BLOCK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_BLOCK', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_POW', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_REQUEST_SET_SIZE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELF_RECONCILIATION_NEEDED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEER_RECONCILIATION_NEEDED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY_FOR_PROTOCOL', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_PROTOCOL', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=348,
  serialized_end=602,
)
_sym_db.RegisterEnumDescriptor(_PEERREQUEST_REQUESTTYPE)


_BLOCKHASH = _descriptor.Descriptor(
  name='BlockHash',
  full_name='overhaul.protos.BlockHash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='overhaul.protos.BlockHash.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=108,
)


_VEGVISIRBLOCK = _descriptor.Descriptor(
  name='VegvisirBlock',
  full_name='overhaul.protos.VegvisirBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vegblock', full_name='overhaul.protos.VegvisirBlock.vegblock', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=167,
)


_PEERREQUEST = _descriptor.Descriptor(
  name='PeerRequest',
  full_name='overhaul.protos.PeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='overhaul.protos.PeerRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_hashes', full_name='overhaul.protos.PeerRequest.target_hashes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blocks_to_add', full_name='overhaul.protos.PeerRequest.blocks_to_add', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PEERREQUEST_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=602,
)


_FRONTIERSET = _descriptor.Descriptor(
  name='FrontierSet',
  full_name='overhaul.protos.FrontierSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_hashes', full_name='overhaul.protos.FrontierSet.block_hashes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=667,
)


_SENDBLOCKCHAINHASHES = _descriptor.Descriptor(
  name='SendBlockchainHashes',
  full_name='overhaul.protos.SendBlockchainHashes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash_set', full_name='overhaul.protos.SendBlockchainHashes.hash_set', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=669,
  serialized_end=737,
)


_SENDBLOCK = _descriptor.Descriptor(
  name='SendBlock',
  full_name='overhaul.protos.SendBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocks', full_name='overhaul.protos.SendBlock.blocks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=739,
  serialized_end=798,
)


_ADDBLOCK = _descriptor.Descriptor(
  name='AddBlock',
  full_name='overhaul.protos.AddBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block', full_name='overhaul.protos.AddBlock.block', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=857,
)


_REQUESTSETSIZE = _descriptor.Descriptor(
  name='RequestSetSize',
  full_name='overhaul.protos.RequestSetSize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rset_size', full_name='overhaul.protos.RequestSetSize.rset_size', index=0,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=859,
  serialized_end=894,
)


_PEERRESPONSE = _descriptor.Descriptor(
  name='PeerResponse',
  full_name='overhaul.protos.PeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frontier_set_response', full_name='overhaul.protos.PeerResponse.frontier_set_response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bc_hashes_response', full_name='overhaul.protos.PeerResponse.bc_hashes_response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_block_response', full_name='overhaul.protos.PeerResponse.send_block_response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_block', full_name='overhaul.protos.PeerResponse.add_block', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r_set_size_response', full_name='overhaul.protos.PeerResponse.r_set_size_response', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='peer_response_types', full_name='overhaul.protos.PeerResponse.peer_response_types',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=897,
  serialized_end=1237,
)

_VEGVISIRBLOCK.fields_by_name['vegblock'].message_type = overhaul_dot_protos_dot_charlottewrapper__pb2._BLOCK
_PEERREQUEST.fields_by_name['type'].enum_type = _PEERREQUEST_REQUESTTYPE
_PEERREQUEST.fields_by_name['target_hashes'].message_type = _BLOCKHASH
_PEERREQUEST.fields_by_name['blocks_to_add'].message_type = _VEGVISIRBLOCK
_PEERREQUEST_REQUESTTYPE.containing_type = _PEERREQUEST
_FRONTIERSET.fields_by_name['block_hashes'].message_type = _BLOCKHASH
_SENDBLOCKCHAINHASHES.fields_by_name['hash_set'].message_type = _BLOCKHASH
_SENDBLOCK.fields_by_name['blocks'].message_type = _VEGVISIRBLOCK
_ADDBLOCK.fields_by_name['block'].message_type = _VEGVISIRBLOCK
_PEERRESPONSE.fields_by_name['frontier_set_response'].message_type = _FRONTIERSET
_PEERRESPONSE.fields_by_name['bc_hashes_response'].message_type = _SENDBLOCKCHAINHASHES
_PEERRESPONSE.fields_by_name['send_block_response'].message_type = _SENDBLOCK
_PEERRESPONSE.fields_by_name['add_block'].message_type = _ADDBLOCK
_PEERRESPONSE.fields_by_name['r_set_size_response'].message_type = _REQUESTSETSIZE
_PEERRESPONSE.oneofs_by_name['peer_response_types'].fields.append(
  _PEERRESPONSE.fields_by_name['frontier_set_response'])
_PEERRESPONSE.fields_by_name['frontier_set_response'].containing_oneof = _PEERRESPONSE.oneofs_by_name['peer_response_types']
_PEERRESPONSE.oneofs_by_name['peer_response_types'].fields.append(
  _PEERRESPONSE.fields_by_name['bc_hashes_response'])
_PEERRESPONSE.fields_by_name['bc_hashes_response'].containing_oneof = _PEERRESPONSE.oneofs_by_name['peer_response_types']
_PEERRESPONSE.oneofs_by_name['peer_response_types'].fields.append(
  _PEERRESPONSE.fields_by_name['send_block_response'])
_PEERRESPONSE.fields_by_name['send_block_response'].containing_oneof = _PEERRESPONSE.oneofs_by_name['peer_response_types']
_PEERRESPONSE.oneofs_by_name['peer_response_types'].fields.append(
  _PEERRESPONSE.fields_by_name['add_block'])
_PEERRESPONSE.fields_by_name['add_block'].containing_oneof = _PEERRESPONSE.oneofs_by_name['peer_response_types']
_PEERRESPONSE.oneofs_by_name['peer_response_types'].fields.append(
  _PEERRESPONSE.fields_by_name['r_set_size_response'])
_PEERRESPONSE.fields_by_name['r_set_size_response'].containing_oneof = _PEERRESPONSE.oneofs_by_name['peer_response_types']
DESCRIPTOR.message_types_by_name['BlockHash'] = _BLOCKHASH
DESCRIPTOR.message_types_by_name['VegvisirBlock'] = _VEGVISIRBLOCK
DESCRIPTOR.message_types_by_name['PeerRequest'] = _PEERREQUEST
DESCRIPTOR.message_types_by_name['FrontierSet'] = _FRONTIERSET
DESCRIPTOR.message_types_by_name['SendBlockchainHashes'] = _SENDBLOCKCHAINHASHES
DESCRIPTOR.message_types_by_name['SendBlock'] = _SENDBLOCK
DESCRIPTOR.message_types_by_name['AddBlock'] = _ADDBLOCK
DESCRIPTOR.message_types_by_name['RequestSetSize'] = _REQUESTSETSIZE
DESCRIPTOR.message_types_by_name['PeerResponse'] = _PEERRESPONSE

BlockHash = _reflection.GeneratedProtocolMessageType('BlockHash', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKHASH,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.BlockHash)
  ))
_sym_db.RegisterMessage(BlockHash)

VegvisirBlock = _reflection.GeneratedProtocolMessageType('VegvisirBlock', (_message.Message,), dict(
  DESCRIPTOR = _VEGVISIRBLOCK,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.VegvisirBlock)
  ))
_sym_db.RegisterMessage(VegvisirBlock)

PeerRequest = _reflection.GeneratedProtocolMessageType('PeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _PEERREQUEST,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.PeerRequest)
  ))
_sym_db.RegisterMessage(PeerRequest)

FrontierSet = _reflection.GeneratedProtocolMessageType('FrontierSet', (_message.Message,), dict(
  DESCRIPTOR = _FRONTIERSET,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.FrontierSet)
  ))
_sym_db.RegisterMessage(FrontierSet)

SendBlockchainHashes = _reflection.GeneratedProtocolMessageType('SendBlockchainHashes', (_message.Message,), dict(
  DESCRIPTOR = _SENDBLOCKCHAINHASHES,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.SendBlockchainHashes)
  ))
_sym_db.RegisterMessage(SendBlockchainHashes)

SendBlock = _reflection.GeneratedProtocolMessageType('SendBlock', (_message.Message,), dict(
  DESCRIPTOR = _SENDBLOCK,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.SendBlock)
  ))
_sym_db.RegisterMessage(SendBlock)

AddBlock = _reflection.GeneratedProtocolMessageType('AddBlock', (_message.Message,), dict(
  DESCRIPTOR = _ADDBLOCK,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.AddBlock)
  ))
_sym_db.RegisterMessage(AddBlock)

RequestSetSize = _reflection.GeneratedProtocolMessageType('RequestSetSize', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSETSIZE,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.RequestSetSize)
  ))
_sym_db.RegisterMessage(RequestSetSize)

PeerResponse = _reflection.GeneratedProtocolMessageType('PeerResponse', (_message.Message,), dict(
  DESCRIPTOR = _PEERRESPONSE,
  __module__ = 'vegvisirprotocol_pb2'
  # @@protoc_insertion_point(class_scope:overhaul.protos.PeerResponse)
  ))
_sym_db.RegisterMessage(PeerResponse)


# @@protoc_insertion_point(module_scope)
