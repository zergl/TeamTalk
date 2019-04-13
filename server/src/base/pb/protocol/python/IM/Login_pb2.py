# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IM.Login.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import IM.BaseDefine_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='IM.Login.proto',
  package='IM.Login',
  serialized_pb=_b('\n\x0eIM.Login.proto\x12\x08IM.Login\x1a\x13IM.BaseDefine.proto\"\x0e\n\x0cIMMsgServReq\"q\n\x0cIMMsgServRsp\x12.\n\x0bresult_code\x18\x01 \x02(\x0e\x32\x19.IM.BaseDefine.ResultType\x12\x10\n\x08prior_ip\x18\x02 \x01(\t\x12\x11\n\tbackip_ip\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\r\"\xad\x01\n\nIMLoginReq\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\x32\n\ronline_status\x18\x03 \x02(\x0e\x32\x1b.IM.BaseDefine.UserStatType\x12.\n\x0b\x63lient_type\x18\x04 \x02(\x0e\x32\x19.IM.BaseDefine.ClientType\x12\x16\n\x0e\x63lient_version\x18\x05 \x01(\t\"\xc8\x01\n\nIMLoginRes\x12\x13\n\x0bserver_time\x18\x01 \x02(\r\x12.\n\x0bresult_code\x18\x02 \x02(\x0e\x32\x19.IM.BaseDefine.ResultType\x12\x15\n\rresult_string\x18\x03 \x01(\t\x12\x32\n\ronline_status\x18\x04 \x01(\x0e\x32\x1b.IM.BaseDefine.UserStatType\x12*\n\tuser_info\x18\x05 \x01(\x0b\x32\x17.IM.BaseDefine.UserInfo\"\r\n\x0bIMLogoutReq\"\"\n\x0bIMLogoutRsp\x12\x13\n\x0bresult_code\x18\x01 \x02(\r\"Q\n\nIMKickUser\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x32\n\x0bkick_reason\x18\x02 \x02(\x0e\x32\x1d.IM.BaseDefine.KickReasonType\"~\n\x10IMDeviceTokenReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x14\n\x0c\x64\x65vice_token\x18\x02 \x02(\t\x12.\n\x0b\x63lient_type\x18\x03 \x01(\x0e\x32\x19.IM.BaseDefine.ClientType\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"8\n\x10IMDeviceTokenRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"$\n\x11IMKickPCClientReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\"9\n\x11IMKickPCClientRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0bresult_code\x18\x02 \x02(\r\"N\n\x0fIMPushShieldReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x15\n\rshield_status\x18\x02 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"c\n\x0fIMPushShieldRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0bresult_code\x18\x02 \x02(\r\x12\x15\n\rshield_status\x18\x03 \x01(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"<\n\x14IMQueryPushShieldReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"h\n\x14IMQueryPushShieldRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0bresult_code\x18\x02 \x02(\r\x12\x15\n\rshield_status\x18\x03 \x01(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\x42\x1b\n\x17\x63om.mogujie.tt.protobufH\x03')
  ,
  dependencies=[IM.BaseDefine_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMMSGSERVREQ = _descriptor.Descriptor(
  name='IMMsgServReq',
  full_name='IM.Login.IMMsgServReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=63,
)


_IMMSGSERVRSP = _descriptor.Descriptor(
  name='IMMsgServRsp',
  full_name='IM.Login.IMMsgServRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_code', full_name='IM.Login.IMMsgServRsp.result_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prior_ip', full_name='IM.Login.IMMsgServRsp.prior_ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backip_ip', full_name='IM.Login.IMMsgServRsp.backip_ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='IM.Login.IMMsgServRsp.port', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=178,
)


_IMLOGINREQ = _descriptor.Descriptor(
  name='IMLoginReq',
  full_name='IM.Login.IMLoginReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='IM.Login.IMLoginReq.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='IM.Login.IMLoginReq.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online_status', full_name='IM.Login.IMLoginReq.online_status', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='IM.Login.IMLoginReq.client_type', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_version', full_name='IM.Login.IMLoginReq.client_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=354,
)


_IMLOGINRES = _descriptor.Descriptor(
  name='IMLoginRes',
  full_name='IM.Login.IMLoginRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_time', full_name='IM.Login.IMLoginRes.server_time', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='IM.Login.IMLoginRes.result_code', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_string', full_name='IM.Login.IMLoginRes.result_string', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online_status', full_name='IM.Login.IMLoginRes.online_status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_info', full_name='IM.Login.IMLoginRes.user_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=557,
)


_IMLOGOUTREQ = _descriptor.Descriptor(
  name='IMLogoutReq',
  full_name='IM.Login.IMLogoutReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=572,
)


_IMLOGOUTRSP = _descriptor.Descriptor(
  name='IMLogoutRsp',
  full_name='IM.Login.IMLogoutRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_code', full_name='IM.Login.IMLogoutRsp.result_code', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=574,
  serialized_end=608,
)


_IMKICKUSER = _descriptor.Descriptor(
  name='IMKickUser',
  full_name='IM.Login.IMKickUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMKickUser.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kick_reason', full_name='IM.Login.IMKickUser.kick_reason', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=691,
)


_IMDEVICETOKENREQ = _descriptor.Descriptor(
  name='IMDeviceTokenReq',
  full_name='IM.Login.IMDeviceTokenReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMDeviceTokenReq.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_token', full_name='IM.Login.IMDeviceTokenReq.device_token', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_type', full_name='IM.Login.IMDeviceTokenReq.client_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Login.IMDeviceTokenReq.attach_data', index=3,
      number=20, type=12, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=819,
)


_IMDEVICETOKENRSP = _descriptor.Descriptor(
  name='IMDeviceTokenRsp',
  full_name='IM.Login.IMDeviceTokenRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMDeviceTokenRsp.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Login.IMDeviceTokenRsp.attach_data', index=1,
      number=20, type=12, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=821,
  serialized_end=877,
)


_IMKICKPCCLIENTREQ = _descriptor.Descriptor(
  name='IMKickPCClientReq',
  full_name='IM.Login.IMKickPCClientReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMKickPCClientReq.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=879,
  serialized_end=915,
)


_IMKICKPCCLIENTRSP = _descriptor.Descriptor(
  name='IMKickPCClientRsp',
  full_name='IM.Login.IMKickPCClientRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMKickPCClientRsp.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='IM.Login.IMKickPCClientRsp.result_code', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=917,
  serialized_end=974,
)


_IMPUSHSHIELDREQ = _descriptor.Descriptor(
  name='IMPushShieldReq',
  full_name='IM.Login.IMPushShieldReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMPushShieldReq.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shield_status', full_name='IM.Login.IMPushShieldReq.shield_status', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Login.IMPushShieldReq.attach_data', index=2,
      number=20, type=12, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=976,
  serialized_end=1054,
)


_IMPUSHSHIELDRSP = _descriptor.Descriptor(
  name='IMPushShieldRsp',
  full_name='IM.Login.IMPushShieldRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMPushShieldRsp.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='IM.Login.IMPushShieldRsp.result_code', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shield_status', full_name='IM.Login.IMPushShieldRsp.shield_status', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Login.IMPushShieldRsp.attach_data', index=3,
      number=20, type=12, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1056,
  serialized_end=1155,
)


_IMQUERYPUSHSHIELDREQ = _descriptor.Descriptor(
  name='IMQueryPushShieldReq',
  full_name='IM.Login.IMQueryPushShieldReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMQueryPushShieldReq.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Login.IMQueryPushShieldReq.attach_data', index=1,
      number=20, type=12, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1157,
  serialized_end=1217,
)


_IMQUERYPUSHSHIELDRSP = _descriptor.Descriptor(
  name='IMQueryPushShieldRsp',
  full_name='IM.Login.IMQueryPushShieldRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='IM.Login.IMQueryPushShieldRsp.user_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='IM.Login.IMQueryPushShieldRsp.result_code', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shield_status', full_name='IM.Login.IMQueryPushShieldRsp.shield_status', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attach_data', full_name='IM.Login.IMQueryPushShieldRsp.attach_data', index=3,
      number=20, type=12, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1219,
  serialized_end=1323,
)

_IMMSGSERVRSP.fields_by_name['result_code'].enum_type = IM.BaseDefine_pb2._RESULTTYPE
_IMLOGINREQ.fields_by_name['online_status'].enum_type = IM.BaseDefine_pb2._USERSTATTYPE
_IMLOGINREQ.fields_by_name['client_type'].enum_type = IM.BaseDefine_pb2._CLIENTTYPE
_IMLOGINRES.fields_by_name['result_code'].enum_type = IM.BaseDefine_pb2._RESULTTYPE
_IMLOGINRES.fields_by_name['online_status'].enum_type = IM.BaseDefine_pb2._USERSTATTYPE
_IMLOGINRES.fields_by_name['user_info'].message_type = IM.BaseDefine_pb2._USERINFO
_IMKICKUSER.fields_by_name['kick_reason'].enum_type = IM.BaseDefine_pb2._KICKREASONTYPE
_IMDEVICETOKENREQ.fields_by_name['client_type'].enum_type = IM.BaseDefine_pb2._CLIENTTYPE
DESCRIPTOR.message_types_by_name['IMMsgServReq'] = _IMMSGSERVREQ
DESCRIPTOR.message_types_by_name['IMMsgServRsp'] = _IMMSGSERVRSP
DESCRIPTOR.message_types_by_name['IMLoginReq'] = _IMLOGINREQ
DESCRIPTOR.message_types_by_name['IMLoginRes'] = _IMLOGINRES
DESCRIPTOR.message_types_by_name['IMLogoutReq'] = _IMLOGOUTREQ
DESCRIPTOR.message_types_by_name['IMLogoutRsp'] = _IMLOGOUTRSP
DESCRIPTOR.message_types_by_name['IMKickUser'] = _IMKICKUSER
DESCRIPTOR.message_types_by_name['IMDeviceTokenReq'] = _IMDEVICETOKENREQ
DESCRIPTOR.message_types_by_name['IMDeviceTokenRsp'] = _IMDEVICETOKENRSP
DESCRIPTOR.message_types_by_name['IMKickPCClientReq'] = _IMKICKPCCLIENTREQ
DESCRIPTOR.message_types_by_name['IMKickPCClientRsp'] = _IMKICKPCCLIENTRSP
DESCRIPTOR.message_types_by_name['IMPushShieldReq'] = _IMPUSHSHIELDREQ
DESCRIPTOR.message_types_by_name['IMPushShieldRsp'] = _IMPUSHSHIELDRSP
DESCRIPTOR.message_types_by_name['IMQueryPushShieldReq'] = _IMQUERYPUSHSHIELDREQ
DESCRIPTOR.message_types_by_name['IMQueryPushShieldRsp'] = _IMQUERYPUSHSHIELDRSP

IMMsgServReq = _reflection.GeneratedProtocolMessageType('IMMsgServReq', (_message.Message,), dict(
  DESCRIPTOR = _IMMSGSERVREQ,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMMsgServReq)
  ))
_sym_db.RegisterMessage(IMMsgServReq)

IMMsgServRsp = _reflection.GeneratedProtocolMessageType('IMMsgServRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMMSGSERVRSP,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMMsgServRsp)
  ))
_sym_db.RegisterMessage(IMMsgServRsp)

IMLoginReq = _reflection.GeneratedProtocolMessageType('IMLoginReq', (_message.Message,), dict(
  DESCRIPTOR = _IMLOGINREQ,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMLoginReq)
  ))
_sym_db.RegisterMessage(IMLoginReq)

IMLoginRes = _reflection.GeneratedProtocolMessageType('IMLoginRes', (_message.Message,), dict(
  DESCRIPTOR = _IMLOGINRES,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMLoginRes)
  ))
_sym_db.RegisterMessage(IMLoginRes)

IMLogoutReq = _reflection.GeneratedProtocolMessageType('IMLogoutReq', (_message.Message,), dict(
  DESCRIPTOR = _IMLOGOUTREQ,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMLogoutReq)
  ))
_sym_db.RegisterMessage(IMLogoutReq)

IMLogoutRsp = _reflection.GeneratedProtocolMessageType('IMLogoutRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMLOGOUTRSP,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMLogoutRsp)
  ))
_sym_db.RegisterMessage(IMLogoutRsp)

IMKickUser = _reflection.GeneratedProtocolMessageType('IMKickUser', (_message.Message,), dict(
  DESCRIPTOR = _IMKICKUSER,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMKickUser)
  ))
_sym_db.RegisterMessage(IMKickUser)

IMDeviceTokenReq = _reflection.GeneratedProtocolMessageType('IMDeviceTokenReq', (_message.Message,), dict(
  DESCRIPTOR = _IMDEVICETOKENREQ,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMDeviceTokenReq)
  ))
_sym_db.RegisterMessage(IMDeviceTokenReq)

IMDeviceTokenRsp = _reflection.GeneratedProtocolMessageType('IMDeviceTokenRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMDEVICETOKENRSP,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMDeviceTokenRsp)
  ))
_sym_db.RegisterMessage(IMDeviceTokenRsp)

IMKickPCClientReq = _reflection.GeneratedProtocolMessageType('IMKickPCClientReq', (_message.Message,), dict(
  DESCRIPTOR = _IMKICKPCCLIENTREQ,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMKickPCClientReq)
  ))
_sym_db.RegisterMessage(IMKickPCClientReq)

IMKickPCClientRsp = _reflection.GeneratedProtocolMessageType('IMKickPCClientRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMKICKPCCLIENTRSP,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMKickPCClientRsp)
  ))
_sym_db.RegisterMessage(IMKickPCClientRsp)

IMPushShieldReq = _reflection.GeneratedProtocolMessageType('IMPushShieldReq', (_message.Message,), dict(
  DESCRIPTOR = _IMPUSHSHIELDREQ,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMPushShieldReq)
  ))
_sym_db.RegisterMessage(IMPushShieldReq)

IMPushShieldRsp = _reflection.GeneratedProtocolMessageType('IMPushShieldRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMPUSHSHIELDRSP,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMPushShieldRsp)
  ))
_sym_db.RegisterMessage(IMPushShieldRsp)

IMQueryPushShieldReq = _reflection.GeneratedProtocolMessageType('IMQueryPushShieldReq', (_message.Message,), dict(
  DESCRIPTOR = _IMQUERYPUSHSHIELDREQ,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMQueryPushShieldReq)
  ))
_sym_db.RegisterMessage(IMQueryPushShieldReq)

IMQueryPushShieldRsp = _reflection.GeneratedProtocolMessageType('IMQueryPushShieldRsp', (_message.Message,), dict(
  DESCRIPTOR = _IMQUERYPUSHSHIELDRSP,
  __module__ = 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMQueryPushShieldRsp)
  ))
_sym_db.RegisterMessage(IMQueryPushShieldRsp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.mogujie.tt.protobufH\003'))
# @@protoc_insertion_point(module_scope)
