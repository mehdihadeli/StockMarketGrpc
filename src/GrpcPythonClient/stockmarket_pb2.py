# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stockmarket.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stockmarket.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\026StockMarket.Grpc.Proto',
  serialized_pb=b'\n\x11stockmarket.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\'\n\x07\x44\x65\x63imal\x12\r\n\x05units\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x0f\"H\n\x0cStockRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12(\n\x04\x64\x61te\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"%\n\x13StockHistoryRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\"\xcc\x01\n\tStockData\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x19\n\x07\x64\x61yOpen\x18\x02 \x01(\x0b\x32\x08.Decimal\x12\x18\n\x06\x64\x61yLow\x18\x03 \x01(\x0b\x32\x08.Decimal\x12\x19\n\x07\x64\x61yHigh\x18\x04 \x01(\x0b\x32\x08.Decimal\x12\x1c\n\nLastChange\x18\x05 \x01(\x0b\x32\x08.Decimal\x12\x17\n\x05price\x18\x06 \x01(\x0b\x32\x08.Decimal\x12(\n\x04\x64\x61te\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x11StockHistoryReply\x12\x1d\n\tstockData\x18\x01 \x03(\x0b\x32\n.StockData\"\xb4\x01\n\nStockReply\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x1b\n\tbestPrice\x18\x02 \x01(\x0b\x32\x08.Decimal\x12\x1c\n\nworstPrice\x18\x03 \x01(\x0b\x32\x08.Decimal\x12,\n\x08\x62\x65stDate\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tworstDate\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x88\x01\n\x11StockPerDateReply\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x1b\n\tbestPrice\x18\x02 \x01(\x0b\x32\x08.Decimal\x12\x1c\n\nworstPrice\x18\x03 \x01(\x0b\x32\x08.Decimal\x12(\n\x04\x64\x61te\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xef\x01\n\x12StockMarketService\x12%\n\x08GetStock\x12\r.StockRequest\x1a\n.StockData\x12;\n\x0fGetStockHistory\x12\x14.StockHistoryRequest\x1a\x12.StockHistoryReply\x12<\n\x14GetStockMarketStream\x12\x16.google.protobuf.Empty\x1a\n.StockData0\x01\x12\x37\n\x0eGetStockStream\x12\r.StockRequest\x1a\x12.StockPerDateReply(\x01\x30\x01\x42\x19\xaa\x02\x16StockMarket.Grpc.Protob\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_DECIMAL = _descriptor.Descriptor(
  name='Decimal',
  full_name='Decimal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='units', full_name='Decimal.units', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nanos', full_name='Decimal.nanos', index=1,
      number=2, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=122,
)


_STOCKREQUEST = _descriptor.Descriptor(
  name='StockRequest',
  full_name='StockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='StockRequest.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='StockRequest.date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=196,
)


_STOCKHISTORYREQUEST = _descriptor.Descriptor(
  name='StockHistoryRequest',
  full_name='StockHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='StockHistoryRequest.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=235,
)


_STOCKDATA = _descriptor.Descriptor(
  name='StockData',
  full_name='StockData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='StockData.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dayOpen', full_name='StockData.dayOpen', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dayLow', full_name='StockData.dayLow', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dayHigh', full_name='StockData.dayHigh', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LastChange', full_name='StockData.LastChange', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='StockData.price', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='StockData.date', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=442,
)


_STOCKHISTORYREPLY = _descriptor.Descriptor(
  name='StockHistoryReply',
  full_name='StockHistoryReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stockData', full_name='StockHistoryReply.stockData', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=494,
)


_STOCKREPLY = _descriptor.Descriptor(
  name='StockReply',
  full_name='StockReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='StockReply.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bestPrice', full_name='StockReply.bestPrice', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worstPrice', full_name='StockReply.worstPrice', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bestDate', full_name='StockReply.bestDate', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worstDate', full_name='StockReply.worstDate', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=677,
)


_STOCKPERDATEREPLY = _descriptor.Descriptor(
  name='StockPerDateReply',
  full_name='StockPerDateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='StockPerDateReply.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bestPrice', full_name='StockPerDateReply.bestPrice', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worstPrice', full_name='StockPerDateReply.worstPrice', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='StockPerDateReply.date', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=816,
)

_STOCKREQUEST.fields_by_name['date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STOCKDATA.fields_by_name['dayOpen'].message_type = _DECIMAL
_STOCKDATA.fields_by_name['dayLow'].message_type = _DECIMAL
_STOCKDATA.fields_by_name['dayHigh'].message_type = _DECIMAL
_STOCKDATA.fields_by_name['LastChange'].message_type = _DECIMAL
_STOCKDATA.fields_by_name['price'].message_type = _DECIMAL
_STOCKDATA.fields_by_name['date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STOCKHISTORYREPLY.fields_by_name['stockData'].message_type = _STOCKDATA
_STOCKREPLY.fields_by_name['bestPrice'].message_type = _DECIMAL
_STOCKREPLY.fields_by_name['worstPrice'].message_type = _DECIMAL
_STOCKREPLY.fields_by_name['bestDate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STOCKREPLY.fields_by_name['worstDate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STOCKPERDATEREPLY.fields_by_name['bestPrice'].message_type = _DECIMAL
_STOCKPERDATEREPLY.fields_by_name['worstPrice'].message_type = _DECIMAL
_STOCKPERDATEREPLY.fields_by_name['date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Decimal'] = _DECIMAL
DESCRIPTOR.message_types_by_name['StockRequest'] = _STOCKREQUEST
DESCRIPTOR.message_types_by_name['StockHistoryRequest'] = _STOCKHISTORYREQUEST
DESCRIPTOR.message_types_by_name['StockData'] = _STOCKDATA
DESCRIPTOR.message_types_by_name['StockHistoryReply'] = _STOCKHISTORYREPLY
DESCRIPTOR.message_types_by_name['StockReply'] = _STOCKREPLY
DESCRIPTOR.message_types_by_name['StockPerDateReply'] = _STOCKPERDATEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Decimal = _reflection.GeneratedProtocolMessageType('Decimal', (_message.Message,), {
  'DESCRIPTOR' : _DECIMAL,
  '__module__' : 'stockmarket_pb2'
  # @@protoc_insertion_point(class_scope:Decimal)
  })
_sym_db.RegisterMessage(Decimal)

StockRequest = _reflection.GeneratedProtocolMessageType('StockRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOCKREQUEST,
  '__module__' : 'stockmarket_pb2'
  # @@protoc_insertion_point(class_scope:StockRequest)
  })
_sym_db.RegisterMessage(StockRequest)

StockHistoryRequest = _reflection.GeneratedProtocolMessageType('StockHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOCKHISTORYREQUEST,
  '__module__' : 'stockmarket_pb2'
  # @@protoc_insertion_point(class_scope:StockHistoryRequest)
  })
_sym_db.RegisterMessage(StockHistoryRequest)

StockData = _reflection.GeneratedProtocolMessageType('StockData', (_message.Message,), {
  'DESCRIPTOR' : _STOCKDATA,
  '__module__' : 'stockmarket_pb2'
  # @@protoc_insertion_point(class_scope:StockData)
  })
_sym_db.RegisterMessage(StockData)

StockHistoryReply = _reflection.GeneratedProtocolMessageType('StockHistoryReply', (_message.Message,), {
  'DESCRIPTOR' : _STOCKHISTORYREPLY,
  '__module__' : 'stockmarket_pb2'
  # @@protoc_insertion_point(class_scope:StockHistoryReply)
  })
_sym_db.RegisterMessage(StockHistoryReply)

StockReply = _reflection.GeneratedProtocolMessageType('StockReply', (_message.Message,), {
  'DESCRIPTOR' : _STOCKREPLY,
  '__module__' : 'stockmarket_pb2'
  # @@protoc_insertion_point(class_scope:StockReply)
  })
_sym_db.RegisterMessage(StockReply)

StockPerDateReply = _reflection.GeneratedProtocolMessageType('StockPerDateReply', (_message.Message,), {
  'DESCRIPTOR' : _STOCKPERDATEREPLY,
  '__module__' : 'stockmarket_pb2'
  # @@protoc_insertion_point(class_scope:StockPerDateReply)
  })
_sym_db.RegisterMessage(StockPerDateReply)


DESCRIPTOR._options = None

_STOCKMARKETSERVICE = _descriptor.ServiceDescriptor(
  name='StockMarketService',
  full_name='StockMarketService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=819,
  serialized_end=1058,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStock',
    full_name='StockMarketService.GetStock',
    index=0,
    containing_service=None,
    input_type=_STOCKREQUEST,
    output_type=_STOCKDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStockHistory',
    full_name='StockMarketService.GetStockHistory',
    index=1,
    containing_service=None,
    input_type=_STOCKHISTORYREQUEST,
    output_type=_STOCKHISTORYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStockMarketStream',
    full_name='StockMarketService.GetStockMarketStream',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_STOCKDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStockStream',
    full_name='StockMarketService.GetStockStream',
    index=3,
    containing_service=None,
    input_type=_STOCKREQUEST,
    output_type=_STOCKPERDATEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STOCKMARKETSERVICE)

DESCRIPTOR.services_by_name['StockMarketService'] = _STOCKMARKETSERVICE

# @@protoc_insertion_point(module_scope)
