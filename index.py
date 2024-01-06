from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.security import OAuth2PasswordRequestForm
from models.client import Client


app = FastAPI()
# Your database URL
DATABASE_URL = 'sqlite:///./data/peaqock.db'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class to handle the database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a Base class for declarative models
Base: DeclarativeMeta = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/clients/{client_id}", response_model=Client)
def get_client_by_id(client_id: int, db: SessionLocal = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client