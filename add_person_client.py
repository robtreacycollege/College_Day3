__author__ = 'williamwong'

import addressbook_pb2

_TIMEOUT_SECONDS = 10


class add_person:
    def PromptForAddress(self, person):
      person.id = int(raw_input("Enter person ID number: "))
      person.name = raw_input("Enter name: ")

      email = raw_input("Enter email address (blank for none): ")
      if email != "":
        person.email = email

      while True:
        number = raw_input("Enter a phone number (or leave blank to finish): ")
        if number == "":
          break

        phone_number = person.phone.add()
        phone_number.number = number

        type = raw_input("Is this a mobile, home, or work phone? ")
        if type == "mobile":
          phone_number.type = addressbook_pb2.Person.MOBILE
        elif type == "home":
          phone_number.type = addressbook_pb2.Person.HOME
        elif type == "work":
          phone_number.type = addressbook_pb2.Person.WORK
        else:
          print "Unknown phone type; leaving as default value."


def run():
  with addressbook_pb2.early_adopter_create_Write_Person_To_File_stub('localhost', 50051) as stub:
    address_book = addressbook_pb2.AddressBook()
    addPerson = add_person()
    #person = addressbook_pb2.Person()


    addPerson.PromptForAddress(address_book.person.add())
    print("test: " + address_book.SerializeToString())

    response = stub.Write_Person(address_book, _TIMEOUT_SECONDS)
    print "LookUpPerson client received: " + response.message


if __name__ == '__main__':
  run()