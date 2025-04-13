from sqlmodel import Session, select
from app.infrastructure.database.models.user_model import UserModel
from app.core.security import hash_password
from app.presentation.schemas.user_schema import UserCreate


def create_user(session: Session, user_data: UserCreate) -> UserModel:
    existing = session.exec(select(UserModel).where(UserModel.email == user_data.email)).first()
    if existing:
        raise ValueError("Email already in use.")

    user = UserModel(
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        role_id=user_data.role_id
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    return user
