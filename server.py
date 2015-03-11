__author__ = 'anngordon'

import time

import addressbook_pb2

import sys

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(addressbook_pb2.EarlyAdopterGreeterServicer):

  def SayHello(self, request, context):
    return addressbook_pb2.HelloReply(message='Hello, %s!' % request.name)






def serve():
  server = addressbook_pb2.early_adopter_create_Greeter_server(
      Greeter(), 50051, None, None)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()
