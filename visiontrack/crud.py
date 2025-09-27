from sqlalchemy.orm import Session
import visiontrack.models as models
import visiontrack.schemas as schemas

def create_project(db: Session, data: schemas.ProjectCreate) -> models.Project:
	obj = models.Project(**data.dict())
	db.add(obj); db.commit(); db.refresh(obj)
	return obj

def get_project(db: Session, project_id: int):
	return db.query(models.Project).filter(models.Project.id == project_id).first()

def list_projects(db: Session, skip=0, limit=100):
	return db.query(models.Project).offset(skip).limit(limit).all()

def delete_project(db: Session, project_id: int) -> bool:
	obj = get_project(db, project_id)
	if not obj: return False
	db.delete(obj); db.commit(); return True

def create_task(db: Session, data: schemas.TaskCreate) -> models.Task:
	obj = models.Task(**data.dict())
	db.add(obj); db.commit(); db.refresh(obj)
	return obj

def list_tasks(db: Session, project_id: int | None = None):
	q = db.query(models.Task)
	if project_id:
		q = q.filter(models.Task.project_id == project_id)
	return q.all()

def create_cost(db: Session, data: schemas.CostCreate) -> models.Cost:
	obj = models.Cost(**data.dict())
	db.add(obj); db.commit(); db.refresh(obj)
	return obj

def list_costs(db: Session, project_id: int | None = None):
	q = db.query(models.Cost)
	if project_id:
		q = q.filter(models.Cost.project_id == project_id)
	return q.all()

def create_scope_change(db: Session, data: schemas.ScopeChangeCreate) -> models.ScopeChange:
	obj = models.ScopeChange(**data.dict())
	db.add(obj); db.commit(); db.refresh(obj)
	return obj

def list_scope_changes(db: Session, project_id: int | None = None):
	q = db.query(models.ScopeChange)
	if project_id:
		q = q.filter(models.ScopeChange.project_id == project_id)
	return q.all()