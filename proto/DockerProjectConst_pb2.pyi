from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REQUEST_TYPE_COMMON: _ClassVar[RequestType]
    REQUEST_TYPE_GRPC: _ClassVar[RequestType]

class ValidUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALID_USER_TYPE_COMMON: _ClassVar[ValidUserType]
    VALID_USER_TYPE_BLACK_LIST: _ClassVar[ValidUserType]
    VALID_USER_TYPE_WHITE_LIST: _ClassVar[ValidUserType]
REQUEST_TYPE_COMMON: RequestType
REQUEST_TYPE_GRPC: RequestType
VALID_USER_TYPE_COMMON: ValidUserType
VALID_USER_TYPE_BLACK_LIST: ValidUserType
VALID_USER_TYPE_WHITE_LIST: ValidUserType
