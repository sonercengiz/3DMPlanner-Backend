from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String
from uuid import UUID, uuid4
from datetime import datetime

class ProjectModel(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))
    user_id: UUID
    created_at: datetime
