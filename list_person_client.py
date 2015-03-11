__author__ = 'anngordon'

import addressbook_pb2

_TIMEOUT_SECONDS = 10
_FILE_NAME = 'storage'


def run():
  with addressbook_pb2.early_adopter_create_List_Person_From_File_stub('localhost', 50051) as stub:
    response = stub.List_Person(addressbook_pb2.Request(message="Hello server"), _TIMEOUT_SECONDS)
    print "List Person client received: " + response.SerializeToString()


if __name__ == '__main__':
  run()