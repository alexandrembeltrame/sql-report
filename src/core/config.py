from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

class Settings(BaseModel):
  DATABASE_URL: str = os.getenv("DATABASE_URL")
  ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
  DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()