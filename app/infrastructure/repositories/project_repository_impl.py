from domain.repositories.project_repository import ProjectRepository
from domain.entities.project import Project
from infrastructure.database.models.project_model import ProjectModel
from sqlmodel import Session
from uuid import UUID


class SQLProjectRepository(ProjectRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, project: Project) -> None:
        model = ProjectModel(
            id=project.id,
            name=project.name,
            user_id=project.user_id,
            created_at=project.created_at
        )
        self.session.add(model)
        self.session.commit()
