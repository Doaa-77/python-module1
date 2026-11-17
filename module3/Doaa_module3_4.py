from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Person(BaseModel):
    name: str
    phone_number: str

saved_person = None

@app.post("/person")
def add_person(person: Person):
    global saved_person

    saved_person = person

    return {
        "message": "Person saved successfully",
        "name": person.name,
        "phone_number": person.phone_number
    }

@app.get("/person/random")
def get_person():
    if saved_person is None:
        return {"error": "No person found"}

    number = random.randint(1, 100)

    return {
        "name": saved_person.name,
        "phone_number": saved_person.phone_number,
        "random_number": number
    }