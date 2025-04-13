from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role_id: Optional[UUID]

class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    is_active: bool
    role_id: Optional[UUID]

    class Config:
        orm_mode = True
