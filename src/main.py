from fastapi import FastAPI
from src.database.connection import Base, engine
from src.api.routes.employee_routes import router as employee_router

# Cria as tabelas no banco se ainda não existirem
Base.metadata.create_all(bind=engine)

# Instância principal da aplicação FastAPI
app = FastAPI(
    title="API de Gestão de Funcionários",
    description="CRUD completo de funcionários com FastAPI + SQLAlchemy",
    version="1.0.0"
)

# Registro das rotas (Routers)
app.include_router(employee_router)


@app.get("/", tags=["Root"])
def read_root():
    """Rota raiz para verificação de status."""
    return {"message": "🚀 API de Gestão de Funcionários está online!"}
