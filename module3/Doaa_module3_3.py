
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextData(BaseModel):
    Text: str

@app.post("/check")
def check_text(data: TextData):
    return {"message": data.Text}