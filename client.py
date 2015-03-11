__author__ = 'anngordon'

import addressbook_pb2

_TIMEOUT_SECONDS = 10


def run():
  with addressbook_pb2.early_adopter_create_Greeter_stub('localhost', 50051) as stub:
    response = stub.SayHello(addressbook_pb2.HelloRequest(name='you'), _TIMEOUT_SECONDS)
    print "Greeter client received: " + response.message


if __name__ == '__main__':
  run()
