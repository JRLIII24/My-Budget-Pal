import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()  # This loads the .env file located at the project root

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://budget_user:securepassword@localhost/budget_app")

class Settings(BaseSettings):
    app_name: str = "My Budget Pal"
    admin_email: str
    items_per_user: int = 50

    class Config:
        env_file = ".env"

settings = Settings()