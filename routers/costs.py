from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/costs", tags=["costs"])

@router.post("", response_model=schemas.CostRead)
def create_cost(payload: schemas.CostCreate, db: Session = Depends(get_db)):
    return crud.create_cost(db, payload)

@router.get("", response_model=list[schemas.CostRead])
def list_costs(project_id: int | None = None, db: Session = Depends(get_db)):
    return crud.list_costs(db, project_id)
