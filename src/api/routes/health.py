from fastapi import APIRouter
from src.api.services.health_services import check_database_connection

router = APIRouter()

@router.get("/health")
def health_check():
    db_status = check_database_connection()
    return {"database": db_status}
