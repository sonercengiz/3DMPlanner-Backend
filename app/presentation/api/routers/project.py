from fastapi import APIRouter, Depends
from uuid import UUID
from application.use_cases.create_project import CreateProjectUseCase
from presentation.schemas.project_schema import CreateProjectRequest, ProjectResponse
from infrastructure.repositories.project_repository_impl import SQLProjectRepository
from infrastructure.database.session import get_session
from sqlmodel import Session


router = APIRouter()

@router.post("/", response_model=ProjectResponse)
def create_project(
    request: CreateProjectRequest,
    user_id: UUID = Depends(...),  # kullanıcı kimliğini buradan çözümle (örnek: JWT'den)
    session: Session = Depends(get_session)
):
    repo = SQLProjectRepository(session)
    use_case = CreateProjectUseCase(repo)
    project = use_case.execute(request.name, user_id)
    return project
