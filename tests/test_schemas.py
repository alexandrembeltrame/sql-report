from datetime import date
from src.schemas.finance_schema import FinanceCreate, FinanceResponse

def test_finance_create():
    finance_data = {
        "date": date(2023, 10, 1),
        "description": "Test transaction",
        "doc_number": "12345",
        "credit": 100.0,
        "debit": 0.0,
    }
    finance = FinanceCreate(**finance_data)
    assert finance.date == finance_data["date"]
    assert finance.description == finance_data["description"]
    assert finance.doc_number == finance_data["doc_number"]
    assert finance.credit == finance_data["credit"]
    assert finance.debit == finance_data["debit"]

def test_finance_response():
    finance_data = {
        "id": 1,
        "date": date(2023, 10, 1),
        "description": "Test transaction",
        "doc_number": "12345",
        "credit": 100.0,
        "debit": 0.0,
    }
    finance = FinanceResponse(**finance_data)
    assert finance.id == finance_data["id"]
    assert finance.date == finance_data["date"]
    assert finance.description == finance_data["description"]
    assert finance.doc_number == finance_data["doc_number"]
    assert finance.credit == finance_data["credit"]
    assert finance.debit == finance_data["debit"]
