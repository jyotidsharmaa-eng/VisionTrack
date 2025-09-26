from datetime import date, datetime
from pydantic import BaseModel, Field

class ProjectBase(BaseModel):
    name: str = Field(..., max_length=200)
    owner: str
    start_date: date
    end_date: date | None = None
    budget: float = 0.0
    description: str | None = None

class ProjectCreate(ProjectBase):
    pass

class ProjectRead(ProjectBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    name: str
    assignee: str | None = None
    planned_hours: float = 0.0
    actual_hours: float = 0.0
    status: str = "planned"
    due_date: date | None = None

class TaskCreate(TaskBase):
    project_id: int

class TaskRead(TaskBase):
    id: int
    project_id: int
    class Config:
        from_attributes = True

class CostBase(BaseModel):
    category: str
    amount: float
    incurred_on: date

class CostCreate(CostBase):
    project_id: int

class CostRead(CostBase):
    id: int
    project_id: int
    class Config:
        from_attributes = True

class ScopeChangeBase(BaseModel):
    version: int = 1
    description: str

class ScopeChangeCreate(ScopeChangeBase):
    project_id: int

class ScopeChangeRead(ScopeChangeBase):
    id: int
    project_id: int
    created_at: datetime
    class Config:
        from_attributes = True
