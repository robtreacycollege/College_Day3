__author__ = 'anngordon'

import time

import addressbook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24



class LookUpPerson(addressbook_pb2.EarlyAdopterLookUpPersonServicer):

  def LookUp(self, request, context):
    return addressbook_pb2.ReplyResponse(message='Hello, %s!' % request.name)


def serve():
  server = addressbook_pb2.early_adopter_create_LookUpPerson_server(
      LookUpPerson(), 50051, None, None)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()
