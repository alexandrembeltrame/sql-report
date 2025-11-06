from sqlalchemy import text
from sqlalchemy.orm import Session

from database.models.employee_model_backup import Employee

def get_employee_report(db: Session):
  """
  Exemplo básico de relatório dinamico
  Retorna todos os funcionários com nome e cargo
  """

  sql = text("""
             SELECT id, name, department, salary, performance
             FROM employees
             ORDER BY id ASC
             """)
  result = db.execute(sql)
  rows = result.fetchall()
  return [dict(row._mapping) for row in rows]