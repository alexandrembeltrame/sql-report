from sqlalchemy import Column, Integer, String, Float
from src.database.connection import Base

class Employee(Base):
  __tablename__ = "employees"
  __table_args__ = {'extend_existing': True}


  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  department = Column(String(50), nullable=False)
  salary = Column(Float, nullable=False)
  performance = Column(Integer, nullable=False)