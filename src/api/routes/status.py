from fastapi import APIRouter
from src.core.config import settings

router = APIRouter()

@router.get("/status")
def get_status():
    return {
        "status": "ok",
        "environment": settings.ENVIRONMENT,
        "debug": settings.DEBUG
    }
