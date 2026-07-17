from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Task:

    name: str

    action: str

    target: str = ""

    payload: dict = field(default_factory=dict)

    priority: int = 5

    status: str = "PENDING"

    task_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    created_at: str = field(
        default_factory=lambda: datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )


    def start(self):

        self.status = "RUNNING"


    def complete(self):

        self.status = "COMPLETED"


    def fail(self):

        self.status = "FAILED"


    def cancel(self):

        self.status = "CANCELLED"


    def to_dict(self):

        return {

            "id": self.task_id,

            "name": self.name,

            "action": self.action,

            "target": self.target,

            "priority": self.priority,

            "status": self.status,

            "payload": self.payload,

            "created_at": self.created_at

        }


    def __repr__(self):

        return (

            f"Task("

            f"{self.name}, "

            f"{self.status}, "

            f"priority={self.priority}"

            f")"

        )
