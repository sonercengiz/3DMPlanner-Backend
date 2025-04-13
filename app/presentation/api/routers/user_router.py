from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.infrastructure.database.session import get_session
from app.presentation.schemas import UserCreate, UserRead
from app.domain.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("", response_model=UserRead)
def register_user(user_data: UserCreate, session: Session = Depends(get_session)):
    try:
        user = create_user(session, user_data)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
