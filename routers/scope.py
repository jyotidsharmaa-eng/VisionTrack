from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/scope", tags=["scope"])

@router.post("", response_model=schemas.ScopeChangeRead)
def create_scope_change(payload: schemas.ScopeChangeCreate, db: Session = Depends(get_db)):
    return crud.create_scope_change(db, payload)

@router.get("", response_model=list[schemas.ScopeChangeRead])
def list_scope_changes(project_id: int | None = None, db: Session = Depends(get_db)):
    return crud.list_scope_changes(db, project_id)
