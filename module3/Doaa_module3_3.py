
import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Create API
app = FastAPI()

# Create POST API
@app.post("/text")
async def receive_text(request: Request):

    # Read JSON data from request
    data = await request.json()

    # Check if Text is missing
    if "Text" not in data:
        return JSONResponse(
            status_code=422,
            content={"error": "Text is missing"}
        )

    # Return successful response
    return {"message": data["Text"]}
