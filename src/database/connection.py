# src/database/connection.py
from sqlalchemy import create_engine, text

DATABASE_URL = "sqlite:///../db.sqlite3"  # caminho relativo à pasta src
engine = create_engine(DATABASE_URL, echo=False, future=True)

def get_connection():
    """
    Retorna um context manager (Connection) pronto para o `with`.
    Uso:
        with get_connection() as conn:
            result = conn.execute(text("SELECT 1"))
    """
    return engine.connect()

if __name__ == "__main__":
    # teste rápido
    with get_connection() as conn:
        r = conn.execute(text("SELECT 1"))
        print(r.fetchall())
