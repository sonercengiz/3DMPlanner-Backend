from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreateProjectRequest(BaseModel):
    name: str


class ProjectResponse(BaseModel):
    id: UUID
    name: str
    user_id: UUID
    created_at: datetime
