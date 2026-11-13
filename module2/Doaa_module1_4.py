
import json

# Step 1: Create a class
class Person:
    def __init__(self, name, number, location, job_title):
        self.name = name
        self.number = number
        self.location = location
        self.job_title = job_title


# Step 2: Create a function to save people
def save_people(people):
    data = []

    for person in people:
        data.append(person.__dict__)

    with open("people.json", "w") as file:
        json.dump(data, file, indent=4)


# Step 3: Create 5 people
person1 = Person("Ahmed", 101, "Abu Dhabi", "Engineer")
person2 = Person("Sara", 102, "Dubai", "Pilot")
person3 = Person("Omar", 103, "Sharjah", "Teacher")
person4 = Person("Mariam", 104, "Fujairah", "Doctor")
person5 = Person("Khalid", 105, "Ajman", "Manager")


# Step 4: Save people in JSON file
people = [person1, person2, person3, person4, person5]

save_people(people)

print("People saved successfully!")