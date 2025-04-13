from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from uuid import UUID, uuid4
from sqlalchemy import Column, String
from app.infrastructure.database.models.role_model import RolePermissionLink


if TYPE_CHECKING:
    from .role_model import RoleModel


class PermissionModel(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False))
    parent_id: Optional[UUID] = Field(default=None, foreign_key="permissionmodel.id")

    children: List["PermissionModel"] = Relationship(
        back_populates="parent",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )

    parent: Optional["PermissionModel"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "PermissionModel.id"}
    )

    roles: List["RoleModel"] = Relationship(
        back_populates="permissions",
        link_model=RolePermissionLink
    )
