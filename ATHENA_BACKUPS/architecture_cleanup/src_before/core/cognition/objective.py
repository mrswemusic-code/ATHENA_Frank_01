from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Objective:

    title: str

    description: str = ""

    priority: int = 5

    status: str = "PENDING"

    objective_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    created_at: str = field(
        default_factory=lambda: datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    metadata: dict = field(
        default_factory=dict
    )

    def start(self):

        self.status = "RUNNING"

    def complete(self):

        self.status = "COMPLETED"

    def fail(self):

        self.status = "FAILED"

    def to_dict(self):

        return {

            "id": self.objective_id,

            "title": self.title,

            "description": self.description,

            "priority": self.priority,

            "status": self.status,

            "created_at": self.created_at,

            "metadata": self.metadata

        }
