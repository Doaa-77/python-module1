from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

# Connect to SQLite database
engine = create_engine("sqlite:///tasks.db")

# Create database base
Base = declarative_base()

# Create table
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)

# Create table if it does not exist
Base.metadata.create_all(bind=engine)

# Create database session
Session = sessionmaker(bind=engine)


# Create POST API
@app.post("/add_people")
def add_people():

    # Open database session
    session = Session()

    # Create 2 people
    person1 = Task(name="Doaa", phone="0501234567")
    person2 = Task(name="Ahmed", phone="0509876543")

    # Add people to database
    session.add(person1)
    session.add(person2)

    # Save changes
    session.commit()

    # Close session
    session.close()

    return {"message": "2 people added successfully"}