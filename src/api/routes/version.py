from fastapi import APIRouter
from src.api.services.version_services import get_version_info

router = APIRouter()

@router.get("/version")
def version():
    return get_version_info()
