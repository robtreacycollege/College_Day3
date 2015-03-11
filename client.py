__author__ = 'anngordon'

import addressbook_pb2

_TIMEOUT_SECONDS = 10


def run():
  with addressbook_pb2.early_adopter_create_LookUpPerson_stub('localhost', 50051) as stub:
    response = stub.LookUp(addressbook_pb2.Person(name='you', id=41247234), _TIMEOUT_SECONDS)
    print "LookUpPerson client received: " + response.message


if __name__ == '__main__':
  run()
