# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addressbook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='addressbook.proto',
  package='tutorial',
  serialized_pb=_b('\n\x11\x61\x64\x64ressbook.proto\x12\x08tutorial\"\xda\x01\n\x06Person\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12+\n\x05phone\x18\x04 \x03(\x0b\x32\x1c.tutorial.Person.PhoneNumber\x1aM\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x02(\t\x12.\n\x04type\x18\x02 \x01(\x0e\x32\x1a.tutorial.Person.PhoneType:\x04HOME\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"/\n\x0b\x41\x64\x64ressBook\x12 \n\x06person\x18\x01 \x03(\x0b\x32\x10.tutorial.Person\" \n\rReplyResponse\x12\x0f\n\x07message\x18\x01 \x02(\t\"\x1a\n\x07Request\x12\x0f\n\x07message\x18\x01 \x02(\t\"!\n\x0eServerResponse\x12\x0f\n\x07message\x18\x01 \x02(\t2E\n\x0cLookUpPerson\x12\x35\n\x06LookUp\x12\x10.tutorial.Person\x1a\x17.tutorial.ReplyResponse\"\x00\x32X\n\x14Write_Person_To_File\x12@\n\x0cWrite_Person\x12\x15.tutorial.AddressBook\x1a\x17.tutorial.ReplyResponse\"\x00\x32R\n\x15List_Person_From_File\x12\x39\n\x0bList_Person\x12\x11.tutorial.Request\x1a\x15.tutorial.AddressBook\"\x00\x32g\n\x1c\x43lient_List_Person_From_File\x12G\n\x12\x43lient_List_Person\x12\x15.tutorial.AddressBook\x1a\x18.tutorial.ServerResponse\"\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PERSON_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='tutorial.Person.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=207,
  serialized_end=250,
)
_sym_db.RegisterEnumDescriptor(_PERSON_PHONETYPE)


_PERSON_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='tutorial.Person.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='tutorial.Person.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='tutorial.Person.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
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
  serialized_start=128,
  serialized_end=205,
)

_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='tutorial.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tutorial.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='tutorial.Person.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='tutorial.Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone', full_name='tutorial.Person.phone', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PERSON_PHONENUMBER, ],
  enum_types=[
    _PERSON_PHONETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=250,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='tutorial.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='tutorial.AddressBook.person', index=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=299,
)


_REPLYRESPONSE = _descriptor.Descriptor(
  name='ReplyResponse',
  full_name='tutorial.ReplyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tutorial.ReplyResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=301,
  serialized_end=333,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='tutorial.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tutorial.Request.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=335,
  serialized_end=361,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='tutorial.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tutorial.ServerResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=363,
  serialized_end=396,
)

_PERSON_PHONENUMBER.fields_by_name['type'].enum_type = _PERSON_PHONETYPE
_PERSON_PHONENUMBER.containing_type = _PERSON
_PERSON.fields_by_name['phone'].message_type = _PERSON_PHONENUMBER
_PERSON_PHONETYPE.containing_type = _PERSON
_ADDRESSBOOK.fields_by_name['person'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
DESCRIPTOR.message_types_by_name['ReplyResponse'] = _REPLYRESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(

  PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
    DESCRIPTOR = _PERSON_PHONENUMBER,
    __module__ = 'addressbook_pb2'
    # @@protoc_insertion_point(class_scope:tutorial.Person.PhoneNumber)
    ))
  ,
  DESCRIPTOR = _PERSON,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Person)
  ))
_sym_db.RegisterMessage(Person)
_sym_db.RegisterMessage(Person.PhoneNumber)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSBOOK,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.AddressBook)
  ))
_sym_db.RegisterMessage(AddressBook)

ReplyResponse = _reflection.GeneratedProtocolMessageType('ReplyResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPLYRESPONSE,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.ReplyResponse)
  ))
_sym_db.RegisterMessage(ReplyResponse)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Request)
  ))
_sym_db.RegisterMessage(Request)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVERRESPONSE,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.ServerResponse)
  ))
_sym_db.RegisterMessage(ServerResponse)


import abc
from grpc.early_adopter import implementations
from grpc.early_adopter import utilities
class EarlyAdopterLookUpPersonServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def LookUp(self, request, context):
    raise NotImplementedError()
class EarlyAdopterLookUpPersonServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterLookUpPersonStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def LookUp(self, request):
    raise NotImplementedError()
  LookUp.async = None
def early_adopter_create_LookUpPerson_server(servicer, port, root_certificates, key_chain_pairs):
  import addressbook_pb2
  import addressbook_pb2
  method_service_descriptions = {
    "LookUp": utilities.unary_unary_service_description(
      servicer.LookUp,
      addressbook_pb2.Person.FromString,
      addressbook_pb2.ReplyResponse.SerializeToString,
    ),
  }
  return implementations.secure_server(method_service_descriptions, port, root_certificates, key_chain_pairs)
def early_adopter_create_LookUpPerson_stub(host, port):
  import addressbook_pb2
  import addressbook_pb2
  method_invocation_descriptions = {
    "LookUp": utilities.unary_unary_invocation_description(
      addressbook_pb2.Person.SerializeToString,
      addressbook_pb2.ReplyResponse.FromString,
    ),
  }
  return implementations.insecure_stub(method_invocation_descriptions, host, port)
class EarlyAdopterWrite_Person_To_FileServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Write_Person(self, request, context):
    raise NotImplementedError()
class EarlyAdopterWrite_Person_To_FileServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterWrite_Person_To_FileStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Write_Person(self, request):
    raise NotImplementedError()
  Write_Person.async = None
def early_adopter_create_Write_Person_To_File_server(servicer, port, root_certificates, key_chain_pairs):
  import addressbook_pb2
  import addressbook_pb2
  method_service_descriptions = {
    "Write_Person": utilities.unary_unary_service_description(
      servicer.Write_Person,
      addressbook_pb2.AddressBook.FromString,
      addressbook_pb2.ReplyResponse.SerializeToString,
    ),
  }
  return implementations.secure_server(method_service_descriptions, port, root_certificates, key_chain_pairs)
def early_adopter_create_Write_Person_To_File_stub(host, port):
  import addressbook_pb2
  import addressbook_pb2
  method_invocation_descriptions = {
    "Write_Person": utilities.unary_unary_invocation_description(
      addressbook_pb2.AddressBook.SerializeToString,
      addressbook_pb2.ReplyResponse.FromString,
    ),
  }
  return implementations.insecure_stub(method_invocation_descriptions, host, port)
class EarlyAdopterList_Person_From_FileServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def List_Person(self, request, context):
    raise NotImplementedError()
class EarlyAdopterList_Person_From_FileServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterList_Person_From_FileStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def List_Person(self, request):
    raise NotImplementedError()
  List_Person.async = None
def early_adopter_create_List_Person_From_File_server(servicer, port, root_certificates, key_chain_pairs):
  import addressbook_pb2
  import addressbook_pb2
  method_service_descriptions = {
    "List_Person": utilities.unary_unary_service_description(
      servicer.List_Person,
      addressbook_pb2.Request.FromString,
      addressbook_pb2.AddressBook.SerializeToString,
    ),
  }
  return implementations.secure_server(method_service_descriptions, port, root_certificates, key_chain_pairs)
def early_adopter_create_List_Person_From_File_stub(host, port):
  import addressbook_pb2
  import addressbook_pb2
  method_invocation_descriptions = {
    "List_Person": utilities.unary_unary_invocation_description(
      addressbook_pb2.Request.SerializeToString,
      addressbook_pb2.AddressBook.FromString,
    ),
  }
  return implementations.insecure_stub(method_invocation_descriptions, host, port)
class EarlyAdopterClient_List_Person_From_FileServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Client_List_Person(self, request, context):
    raise NotImplementedError()
class EarlyAdopterClient_List_Person_From_FileServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterClient_List_Person_From_FileStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Client_List_Person(self, request):
    raise NotImplementedError()
  Client_List_Person.async = None
def early_adopter_create_Client_List_Person_From_File_server(servicer, port, root_certificates, key_chain_pairs):
  import addressbook_pb2
  import addressbook_pb2
  method_service_descriptions = {
    "Client_List_Person": utilities.unary_unary_service_description(
      servicer.Client_List_Person,
      addressbook_pb2.AddressBook.FromString,
      addressbook_pb2.ServerResponse.SerializeToString,
    ),
  }
  return implementations.secure_server(method_service_descriptions, port, root_certificates, key_chain_pairs)
def early_adopter_create_Client_List_Person_From_File_stub(host, port):
  import addressbook_pb2
  import addressbook_pb2
  method_invocation_descriptions = {
    "Client_List_Person": utilities.unary_unary_invocation_description(
      addressbook_pb2.AddressBook.SerializeToString,
      addressbook_pb2.ServerResponse.FromString,
    ),
  }
  return implementations.insecure_stub(method_invocation_descriptions, host, port)
# @@protoc_insertion_point(module_scope)
