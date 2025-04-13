from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.infrastructure.database.session import get_session
from app.infrastructure.database.seeders.permission_seeder import seed_permissions
from app.infrastructure.database.seeders.role_seeder import seed_roles
from app.presentation.api.routers import auth_router, user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: seed işlemleri burada yapılır
    with next(get_session()) as session:
        seed_permissions(session)
        seed_roles(session)
    yield
    # Shutdown: istersen burada loglama vs yapabilirsin


app = FastAPI(lifespan=lifespan)
app.include_router(user_router.router)
app.include_router(auth_router.router)
