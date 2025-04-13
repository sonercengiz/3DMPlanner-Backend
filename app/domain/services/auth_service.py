from sqlmodel import Session, select
from app.infrastructure.database.models.user_model import UserModel
from app.core.security import verify_password
from app.core.jwt import create_access_token


def authenticate_user(session: Session, email: str, password: str) -> str:
    user = session.exec(select(UserModel).where(UserModel.email == email)).first()
    if not user or not verify_password(password, user.password_hash):
        raise ValueError("Invalid credentials")

    token = create_access_token({"sub": str(user.id)})
    return token
