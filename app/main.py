from fastapi import FastAPI

from app.db.database import engine
from app.db.models import Base
from app.routes.patient_routes import router as patient_router
from app.routes.city_routes import router as city_router

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Patient CRUD API")

# Register routes
app.include_router(patient_router)
app.include_router(city_router)