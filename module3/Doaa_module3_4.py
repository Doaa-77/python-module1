
from fastapi import FastAPI
import random

# Create FastAPI application
app = FastAPI()

# Create dictionary to store person information
person = {}

# POST API to receive person information
@app.post("/person")
def add_person(name: str, phone: str):

    # Save name and phone number
    person["name"] = name
    person["phone"] = phone

    return {"message": "Person saved successfully"}


# GET API to read person information
@app.get("/person")
def read_person():

    # Check if person information exists
    if not person:
        return {"error": "No person found"}

    # Generate a random number
    number = random.randint(1, 100)

    # Display person information and random number
    return {
        "name": person["name"],
        "phone": person["phone"],
        "random_number": number
    }