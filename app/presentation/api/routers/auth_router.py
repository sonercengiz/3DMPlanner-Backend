from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.domain.services.auth_service import authenticate_user
from app.infrastructure.database.session import get_session
from app.presentation.schemas.auth_schema import TokenRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(data: TokenRequest, session: Session = Depends(get_session)):
    try:
        token = authenticate_user(session, data.email, data.password)
        return TokenResponse(access_token=token)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
