from fastapi import FastAPI
import random

app = FastAPI()


person_store = {}

@app.post("/person")
def add_person(name: str, phone: str):
    person_store["name"] = name
    person_store["phone"] = phone
    return {"message": "Person saved"}

@app.post("/person/show")
def show_person():
    if not person_store:
        return {"error": "No person found"}

    random_number = random.randint(1, 100)

    return {
        "name": person_store["name"],
        "phone": person_store["phone"],
        "random_number": random_number
    }



