from uuid import UUID
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Project:
    id: UUID
    name: str
    user_id: UUID
    created_at: datetime
