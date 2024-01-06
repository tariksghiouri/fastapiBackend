from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Your database URL
DATABASE_URL = 'sqlite:///./fastapiBackend/data/database.db'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class to handle the database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a Base class for declarative models
Base: DeclarativeMeta = declarative_base()
