# src/database/queries.py
from sqlalchemy import text
from src.database.connection import get_connection

def get_all_employees():
    with get_connection() as conn:
        q = text("SELECT id, name, department, salary, performance FROM employees")
        return [dict(row._mapping) for row in conn.execute(q).all()]

def get_team(department_name: str):
    with get_connection() as conn:
        q = text("""
            SELECT name, salary, performance
            FROM employees
            WHERE department = :department
            ORDER BY name
        """)
        rows = conn.execute(q, {"department": department_name}).all()
        return [tuple(r) for r in rows]  # retorna lista de tuples (name, salary, perf)

def get_top_performers(limit: int = 3):
    with get_connection() as conn:
        q = text("""
            SELECT name, department, performance
            FROM employees
            ORDER BY performance DESC
            LIMIT :limit
        """)
        rows = conn.execute(q, {"limit": limit}).all()
        return [tuple(r) for r in rows]
