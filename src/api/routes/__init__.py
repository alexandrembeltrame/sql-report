from fastapi import APIRouter
from src.api.routes import (
  employee_routes,
  report_routes,
  health,
  status,
  version,
)

router = APIRouter()

router.include_router(employee_routes.router)
router.include_router(report_routes.router)
router.include_router(health.router)
router.include_router(status.router)
router.include_router(version.router)