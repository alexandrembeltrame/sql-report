import sqlite3

def check_database_connection():
  try:
    conn = sqlite3.connect("src/database/company.db")
    conn.execute("SELECT 1")
    conn.close()
    return "connected"
  except Exception as e:
    return f"error: {str(e)}"
