from uuid import uuid4
from datetime import datetime
from domain.entities.project import Project
from domain.repositories.project_repository import ProjectRepository


class CreateProjectUseCase:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def execute(self, name: str, user_id: str):
        project = Project(
            id=uuid4(),
            name=name,
            user_id=user_id,
            created_at=datetime.utcnow()
        )
        self.project_repository.create(project)
        return project
