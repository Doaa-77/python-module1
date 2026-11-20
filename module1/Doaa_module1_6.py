class Person:

 # Store person information
    def __init__(self, name, contact, address, phone_number):
        self.name = name
        self.contact = contact
        self.address = address
        self.phone_number = phone_number

 # Save information in a text file
    def save(self):
        file = open("addresses.text", "a")
        file.write(self.name + "," + self.contact + "," + self.address + "," + self.phone_number)
        file.close()

# Get information from the user
def get_input():
    name = input("Enter name: ")
    contact = input("Enter your email: ")
    address = input("Enter address details: ")
    phone_number = input("Enter phone number: ")

    return Person(name, contact, address, phone_number)
  # Create and return a Person object (Doaa,....)


# Save the user's information
def save_input():
    person = get_input()
    person.save()


save_input()