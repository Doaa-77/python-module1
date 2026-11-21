
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

# Create FastAPI application
app = FastAPI()

# Create POST API
@app.post("/text")
async def check_text(request: Request):

    try:
        # Read JSON data from request
        data = await request.json()

        # Check if data is a dictionary and Text exists
        if not isinstance(data, dict) or "Text" not in data:
            return JSONResponse(
                status_code=422,
                content={"error": "Text is missing"}
            )

        # Check if Text is a string
        if not isinstance(data["Text"], str):
            return JSONResponse(
                status_code=400,
                content={"error": "Text must be a string"}
            )

        # Return success if Text is valid
        return {
            "message": "Success",
            "Text": data["Text"]
        }

    # Handle invalid JSON
    except json.JSONDecodeError:
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid JSON"}
        )
