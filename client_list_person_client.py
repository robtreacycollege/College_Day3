__author__ = 'anngordon'

import addressbook_pb2

_TIMEOUT_SECONDS = 10
_FILE_NAME = 'output'


def run():
  # with addressbook_pb2.early_adopter_create_List_Person_From_File_stub('localhost', 50051) as stub:
  with addressbook_pb2.early_adopter_create_Client_List_Person_From_File_stub('localhost', 50051) as stub:
    address_book = addressbook_pb2.AddressBook()
    print("before reading in from file")
    # Read the existing address book.
    f = open(_FILE_NAME, "rb")
    address_book.ParseFromString(f.read())
    f.close()
    print("after reading in from file, before sending to server")

    # response = stub.Client_List_Person(addressbook_pb2.Request(message="Hello server"), _TIMEOUT_SECONDS)
    response = stub.Client_List_Person(address_book, _TIMEOUT_SECONDS)
    print "List Person client received: " + response.SerializeToString()


if __name__ == '__main__':
  run()