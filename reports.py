from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models import Project, Cost, Task

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/kpis")
def kpis(db: Session = Depends(get_db)):
    total_projects = db.query(Project).count()
    total_cost = db.query(func.coalesce(func.sum(Cost.amount), 0)).scalar() or 0
    total_actual_hours = db.query(func.coalesce(func.sum(Task.actual_hours), 0)).scalar() or 0
    return {
        "total_projects": total_projects,
        "total_cost": total_cost,
        "total_actual_hours": total_actual_hours
    }
