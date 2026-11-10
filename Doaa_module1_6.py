# Create a class to save person information
class Person:

    def __init__(self, name, contact, address, phone_number):
        self.name = name
        self.contact = contact
        self.address = address
        self.phone_number = phone_number

    # Save information in a text file
    def save_to_file(self):
        with open("addresses.text", "a", encoding="utf-8") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Contact: {self.contact}\n")
            file.write(f"Address: {self.address}\n")
            file.write(f"Phone Number: {self.phone_number}\n")
            file.write("----------------------\n")


# Create a function to get user information
def add_person():

    name = input("Enter your name: ")
    contact = input("Enter your contact: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")

    person = Person(name, contact, address, phone_number)

    person.save_to_file()

    print("Information saved successfully!")


# Demo
add_person()