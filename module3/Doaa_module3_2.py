from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/message")
def send_message(data: Message):
    timestamp = datetime.now().isoformat(timespec="seconds")

    return {
        "message": data.message,
        "timestamp": timestamp
    }