from fastapi import FastAPI
from app.routes.patient_routes import router

app = FastAPI(title="Patient CRUD API")

app.include_router(router)