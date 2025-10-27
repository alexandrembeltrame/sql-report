from fastapi import FastAPI
from src.api.routes import status

app = FastAPI(title="SQL Report API")

# registra a rota /status
app.include_router(status.router)

@app.get("/")
def root():
    return {"message": "API SQL Report funcionando!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=True)
