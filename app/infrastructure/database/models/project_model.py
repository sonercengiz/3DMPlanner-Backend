from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime


class ProjectModel(SQLModel, table=True):
    id: UUID = Field(default_factory=UUID, primary_key=True)
    name: str
    user_id: UUID
    created_at: datetime
