
class Person:
    def __init__(self, name, contact, address, phone):
        self.name = name
        self.contact = contact
        self.address = address
        self.phone = phone


name = input("Enter name: ")
contact = input("Enter contact: ")
address = input("Enter address: ")
phone = input("Enter phone number: ")

person = Person(name, contact, address, phone)

file = open("address.txt", "w")
file.write(person.name + "\n")
file.write(person.contact + "\n")
file.write(person.address + "\n")
file.write(person.phone + "\n")
file.close()

print("Address saved successfully!")