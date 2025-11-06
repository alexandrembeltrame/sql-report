from fastapi import FastAPI
from src.database.connection import Base, engine
from src.api.routes.employee_routes import router as employee_router
from src.api.routes.report_routes import router as report_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API SQL Report",
    description="API para consulta de relatórios armazenados no Postgres",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_router)
app.include_router(report_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "🚀 API SQL Report está online!"}
