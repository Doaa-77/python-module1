from fastapi import FastAPI, Request
import logging

app = FastAPI()

# Set up logging to save information in a file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler("my_file.log"),
        logging.StreamHandler()
    ]
)

# Create logger
logger = logging.getLogger(__name__)


# Middleware to log every request
@app.middleware("http")
async def log_requests(request: Request, call_next):

    response = await call_next(request)

    # Get request information
    method = request.method
    path = request.url.path
    status = response.status_code

    # Print information to console and save it in the file
    logger.info(f"{method} {path} {status}")

    return response


@app.get("/hello")
def hello():
    return {"message": "Hello Doaa"}

