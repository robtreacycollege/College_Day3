__author__ = 'anngordon'

import time

import addressbook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_FILE_NAME = 'output'


class Client_List_Person_From_File(addressbook_pb2.EarlyAdopterClient_List_Person_From_FileServicer):

  def Client_List_Person(self, request, context):

      print("On server before print out details")
      print(request.SerializeToString())
      print("On server before returning")
      return addressbook_pb2.ServerResponse(message='Server Response: Success write out')


def serve():
  server = addressbook_pb2.early_adopter_create_Client_List_Person_From_File_server(
      Client_List_Person_From_File(), 50051, None, None)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()