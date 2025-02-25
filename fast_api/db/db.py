import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Retrieve DATABASE_URL from .env, fallback to default for local development
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set. Check your .env file!")

try:
    # Create the database engine
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    # Create session factory
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Base class for SQLAlchemy ORM models
    Base = declarative_base()

except exc.SQLAlchemyError as e:
    raise RuntimeError(f"❌ Database connection error: {e}")

def get_db():
    """Dependency function to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()