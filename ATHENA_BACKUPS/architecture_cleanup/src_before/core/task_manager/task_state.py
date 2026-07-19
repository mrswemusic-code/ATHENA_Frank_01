from enum import Enum


class TaskState(Enum):

    PENDING = "PENDING"

    QUEUED = "QUEUED"

    RUNNING = "RUNNING"

    PAUSED = "PAUSED"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    CANCELLED = "CANCELLED"
