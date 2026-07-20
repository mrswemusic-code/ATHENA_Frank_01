from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Task:

    name: str

    action: str

    target: str = ""

    payload: dict = field(
        default_factory=dict
    )

    priority: int = 5

    agent: str = ""

    status: str = "PENDING"

    result: object = None

    error: str | None = None

    task_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    started_at: str | None = None

    finished_at: str | None = None


    def start(self):

        self.status = "RUNNING"

        self.started_at = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )


    def complete(self, result=None):

        self.status = "COMPLETED"

        self.result = result

        self.finished_at = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )


    def fail(self, error=None):

        self.status = "FAILED"

        self.error = str(error)

        self.finished_at = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )


    def cancel(self):

        self.status = "CANCELLED"

        self.finished_at = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )


    def to_dict(self):

        return {

            "id": self.task_id,

            "name": self.name,

            "action": self.action,

            "target": self.target,

            "agent": self.agent,

            "priority": self.priority,

            "status": self.status,

            "payload": self.payload,

            "result": self.result,

            "error": self.error,

            "created_at": self.created_at,

            "started_at": self.started_at,

            "finished_at": self.finished_at

        }


    def __repr__(self):

        return (

            f"Task("

            f"{self.name}, "

            f"{self.status}, "

            f"agent={self.agent}"

            f")"

        )
