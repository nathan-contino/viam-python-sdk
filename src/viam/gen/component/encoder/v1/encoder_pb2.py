"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 2, '', 'component/encoder/v1/encoder.proto')
_sym_db = _symbol_database.Default()
from ....common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"component/encoder/v1/encoder.proto\x12\x19viam.component.encoder.v1\x1a\x16common/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xbc\x01\n\x12GetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12Q\n\rposition_type\x18\x02 \x01(\x0e2\'.viam.component.encoder.v1.PositionTypeH\x00R\x0cpositionType\x88\x01\x01\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extraB\x10\n\x0e_position_type"y\n\x13GetPositionResponse\x12\x14\n\x05value\x18\x01 \x01(\x02R\x05value\x12L\n\rposition_type\x18\x02 \x01(\x0e2\'.viam.component.encoder.v1.PositionTypeR\x0cpositionType"Y\n\x14ResetPositionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x17\n\x15ResetPositionResponse"Y\n\x14GetPropertiesRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05extra\x18c \x01(\x0b2\x17.google.protobuf.StructR\x05extra"\x83\x01\n\x15GetPropertiesResponse\x122\n\x15ticks_count_supported\x18\x01 \x01(\x08R\x13ticksCountSupported\x126\n\x17angle_degrees_supported\x18\x02 \x01(\x08R\x15angleDegreesSupported*m\n\x0cPositionType\x12\x1d\n\x19POSITION_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19POSITION_TYPE_TICKS_COUNT\x10\x01\x12\x1f\n\x1bPOSITION_TYPE_ANGLE_DEGREES\x10\x022\xc7\x06\n\x0eEncoderService\x12\xa8\x01\n\x0bGetPosition\x12-.viam.component.encoder.v1.GetPositionRequest\x1a..viam.component.encoder.v1.GetPositionResponse":\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/encoder/{name}/get_position\x12\xb0\x01\n\rResetPosition\x12/.viam.component.encoder.v1.ResetPositionRequest\x1a0.viam.component.encoder.v1.ResetPositionResponse"<\x82\xd3\xe4\x93\x026\x124/viam/api/v1/component/encoder/{name}/reset_position\x12\xb0\x01\n\rGetProperties\x12/.viam.component.encoder.v1.GetPropertiesRequest\x1a0.viam.component.encoder.v1.GetPropertiesResponse"<\x82\xd3\xe4\x93\x026"4/viam/api/v1/component/encoder/{name}/get_properties\x12\x8a\x01\n\tDoCommand\x12 .viam.common.v1.DoCommandRequest\x1a!.viam.common.v1.DoCommandResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/encoder/{name}/do_command\x12\x96\x01\n\rGetGeometries\x12$.viam.common.v1.GetGeometriesRequest\x1a%.viam.common.v1.GetGeometriesResponse"8\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/encoder/{name}/geometriesBE\n\x1dcom.viam.component.encoder.v1Z$go.viam.com/api/component/encoder/v1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.encoder.v1.encoder_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.viam.component.encoder.v1Z$go.viam.com/api/component/encoder/v1'
    _globals['_ENCODERSERVICE'].methods_by_name['GetPosition']._loaded_options = None
    _globals['_ENCODERSERVICE'].methods_by_name['GetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/viam/api/v1/component/encoder/{name}/get_position'
    _globals['_ENCODERSERVICE'].methods_by_name['ResetPosition']._loaded_options = None
    _globals['_ENCODERSERVICE'].methods_by_name['ResetPosition']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/viam/api/v1/component/encoder/{name}/reset_position'
    _globals['_ENCODERSERVICE'].methods_by_name['GetProperties']._loaded_options = None
    _globals['_ENCODERSERVICE'].methods_by_name['GetProperties']._serialized_options = b'\x82\xd3\xe4\x93\x026"4/viam/api/v1/component/encoder/{name}/get_properties'
    _globals['_ENCODERSERVICE'].methods_by_name['DoCommand']._loaded_options = None
    _globals['_ENCODERSERVICE'].methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/encoder/{name}/do_command'
    _globals['_ENCODERSERVICE'].methods_by_name['GetGeometries']._loaded_options = None
    _globals['_ENCODERSERVICE'].methods_by_name['GetGeometries']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/viam/api/v1/component/encoder/{name}/geometries'
    _globals['_POSITIONTYPE']._serialized_start = 804
    _globals['_POSITIONTYPE']._serialized_end = 913
    _globals['_GETPOSITIONREQUEST']._serialized_start = 150
    _globals['_GETPOSITIONREQUEST']._serialized_end = 338
    _globals['_GETPOSITIONRESPONSE']._serialized_start = 340
    _globals['_GETPOSITIONRESPONSE']._serialized_end = 461
    _globals['_RESETPOSITIONREQUEST']._serialized_start = 463
    _globals['_RESETPOSITIONREQUEST']._serialized_end = 552
    _globals['_RESETPOSITIONRESPONSE']._serialized_start = 554
    _globals['_RESETPOSITIONRESPONSE']._serialized_end = 577
    _globals['_GETPROPERTIESREQUEST']._serialized_start = 579
    _globals['_GETPROPERTIESREQUEST']._serialized_end = 668
    _globals['_GETPROPERTIESRESPONSE']._serialized_start = 671
    _globals['_GETPROPERTIESRESPONSE']._serialized_end = 802
    _globals['_ENCODERSERVICE']._serialized_start = 916
    _globals['_ENCODERSERVICE']._serialized_end = 1755