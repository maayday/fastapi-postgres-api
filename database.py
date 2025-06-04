from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load .env file to get the DATABASE_URL
load_dotenv()

# Pull the connection string from the .env file
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine for PostgreSQL
engine = create_engine(DATABASE_URL)

# SessionLocal is our DB session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
