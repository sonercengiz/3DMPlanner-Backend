from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.project import Project


class ProjectRepository(ABC):
    @abstractmethod
    def create(self, project: Project) -> None:
        ...
