from sqlalchemy import text
from src.database.connection import SessionLocal

def check_database_connection():
  try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))
    db.close()
    
    return "connected"
  except Exception as e:
    return f"error: {str(e)}"
