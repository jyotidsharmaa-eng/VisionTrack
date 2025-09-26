from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("", response_model=schemas.TaskRead)
def create_task(payload: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, payload)

@router.get("", response_model=list[schemas.TaskRead])
def list_tasks(project_id: int | None = None, db: Session = Depends(get_db)):
    return crud.list_tasks(db, project_id)
