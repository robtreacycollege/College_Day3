__author__ = 'williamwong'

import time
import sys

import addressbook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_FILE_NAME = 'storage'



class Write_Person_To_File(addressbook_pb2.EarlyAdopterWrite_Person_To_FileServicer):

  def Write_Person(self, request, context):
      print("write person in server")
      print(request.SerializeToString())
      f = open(_FILE_NAME, "wb")
      f.write(request.SerializeToString())
      f.close()
      print("Print before return in server" + request.SerializeToString())
      return addressbook_pb2.ReplyResponse(message='Success write')


def serve():
  server = addressbook_pb2.early_adopter_create_Write_Person_To_File_server(
      Write_Person_To_File(), 50051, None, None)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()