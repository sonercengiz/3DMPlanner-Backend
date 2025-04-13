from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from typing import Optional
from sqlalchemy import Column, String, Boolean
from app.infrastructure.database.models.role_model import RoleModel

class UserModel(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(sa_column=Column(String, unique=True, nullable=False))
    password_hash: str = Field(sa_column=Column(String, nullable=False))
    is_active: bool = Field(default=True)
    role_id: Optional[UUID] = Field(default=None, foreign_key="rolemodel.id")

    role: Optional[RoleModel] = Relationship(back_populates="users")
