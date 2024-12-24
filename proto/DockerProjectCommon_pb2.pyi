from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestHeader(_message.Message):
    __slots__ = ("reqSeq", "source")
    REQSEQ_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    reqSeq: str
    source: str
    def __init__(self, reqSeq: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class ResponseHeader(_message.Message):
    __slots__ = ("errno", "errmsg")
    ERRNO_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    errno: int
    errmsg: str
    def __init__(self, errno: _Optional[int] = ..., errmsg: _Optional[str] = ...) -> None: ...

class GetItemInfoReq(_message.Message):
    __slots__ = ("reqHeader", "itemId")
    REQHEADER_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    reqHeader: RequestHeader
    itemId: int
    def __init__(self, reqHeader: _Optional[_Union[RequestHeader, _Mapping]] = ..., itemId: _Optional[int] = ...) -> None: ...

class GetItemInfoResp(_message.Message):
    __slots__ = ("respHeader", "id", "itemSourceName", "itemCnName", "sellOnlineCount", "picUrl", "prices", "currency", "addtime", "modifytime")
    RESPHEADER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMSOURCENAME_FIELD_NUMBER: _ClassVar[int]
    ITEMCNNAME_FIELD_NUMBER: _ClassVar[int]
    SELLONLINECOUNT_FIELD_NUMBER: _ClassVar[int]
    PICURL_FIELD_NUMBER: _ClassVar[int]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ADDTIME_FIELD_NUMBER: _ClassVar[int]
    MODIFYTIME_FIELD_NUMBER: _ClassVar[int]
    respHeader: ResponseHeader
    id: int
    itemSourceName: str
    itemCnName: str
    sellOnlineCount: int
    picUrl: str
    prices: float
    currency: str
    addtime: int
    modifytime: str
    def __init__(self, respHeader: _Optional[_Union[ResponseHeader, _Mapping]] = ..., id: _Optional[int] = ..., itemSourceName: _Optional[str] = ..., itemCnName: _Optional[str] = ..., sellOnlineCount: _Optional[int] = ..., picUrl: _Optional[str] = ..., prices: _Optional[float] = ..., currency: _Optional[str] = ..., addtime: _Optional[int] = ..., modifytime: _Optional[str] = ...) -> None: ...
