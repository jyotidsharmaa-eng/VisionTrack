import pandas as pd

from fastapi import FastAPI, Header, HTTPException, Depends
from config import settings
from database import Base, engine
from projects import router as projects_router
from tasks import router as tasks_router
from costs import router as costs_router
from scope import router as scope_router
from reports import router as reports_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

# Add the /costs-data endpoint after app is defined
@app.get("/costs-data")
def get_costs_data():
    df = pd.read_csv("CostTimeDataset.csv")
    return df.to_dict(orient="records")

# Add the /schedule-data endpoint after app is defined
@app.get("/schedule-data")
def get_schedule_data():
    df = pd.read_csv("TimescheduleDataset.csv")
    return df.to_dict(orient="records")

# Add the /costs-data endpoint after app is defined
@app.get("/costs-data")
def get_costs_data():
    df = pd.read_csv("CostTimeDataset.csv")
    return df.to_dict(orient="records")

# Add the /costs-data endpoint after app is defined
@app.get("/costs-data")
def get_costs_data():
    df = pd.read_csv("CostTimeDataset.csv")
    return df.to_dict(orient="records")
@app.get("/")
def root():
    return {"message": "Welcome to VisionTrack API! Visit /docs for API documentation."}

def verify_api_key(x_api_key: str | None = Header(default=None)):
    if settings.api_key and x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

@app.get("/health")
def health():
    return {"status": "ok", "env": settings.env}

app.include_router(projects_router)
app.include_router(tasks_router)
app.include_router(costs_router)
app.include_router(scope_router)
app.include_router(reports_router)
