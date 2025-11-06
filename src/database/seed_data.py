# src/database/seed_data.py
from sqlalchemy import text
from src.database.connection import SessionLocal

def seed():
    schema = """
   CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL,
    performance INTEGER NOT NULL
);

    """
    data = [
        ("João", "Financeiro", 5500, 88),
        ("Maria", "Financeiro", 6100, 92),
        ("Pedro", "TI", 7200, 85),
        ("Ana", "TI", 7800, 97),
        ("Rafaela", "RH", 5100, 76),
        ("Lucas", "RH", 5300, 81),
        ("Marcos", "Vendas", 6200, 89),
        ("Julia", "Vendas", 6700, 95),
    ]

    db = SessionLocal()
    try:
        db.execute(text(schema))
        db.execute(text("DELETE FROM employees"))
        for name, dept, sal, perf in data:
            db.execute(
                text(
                    """
                    INSERT INTO employees (name, department, salary, performance)
                    VALUES (:name, :dept, :sal, :perf)
                    """
                ),
                {"name": name, "dept": dept, "sal": sal, "perf": perf},
            )
        db.commit()
        print("✅ Banco populado com sucesso.")
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao popular banco: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
