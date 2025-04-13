from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from uuid import UUID, uuid4
from sqlalchemy import Column, String

class RolePermissionLink(SQLModel, table=True):
    role_id: UUID = Field(foreign_key="rolemodel.id", primary_key=True)
    permission_id: UUID = Field(foreign_key="permissionmodel.id", primary_key=True)


class RoleModel(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))

    permissions: List["PermissionModel"] = Relationship(
        back_populates="roles", link_model=RolePermissionLink
    )
    
    users: list["UserModel"] = Relationship(back_populates="role")
