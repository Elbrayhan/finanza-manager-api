from fastapi import FastAPI
from app.database import create_db_and_tables
from app.api.v1 import debts

app = FastAPI(
    title="Finance Manager API 2026",
    description="Sistema avanzado de gestión de deudas y gastos",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(debts.router)
