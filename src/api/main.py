from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import status, health, version, employee_routes, report_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SQL Report API",
    version="1.0.0",
    description="API para geração de relatórios corporativos"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# registra a rota /status
app.include_router(status.router)
app.include_router(health.router)
app.include_router(version.router)
app.include_router(employee_routes.router)
app.include_router(report_routes.router)

@app.get("/")
def root():
    return {"message": "API SQL Report funcionando!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=True)
