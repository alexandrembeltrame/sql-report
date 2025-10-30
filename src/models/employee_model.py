from sqlalchemy import Column, Integer, String, Float
from src.database.connection import Base

class Employee(Base):
  __tablename__ = "employees"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=False)
  department = Column(String(50), nullable=False)
  salary = Column(Float, nullable=False)
  performance = Column(Integer, nullable=False)