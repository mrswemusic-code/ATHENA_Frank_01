from dataclasses import dataclass, field

from uuid import uuid4

import time

from src.core.task_manager.task_state import TaskState

from src.core.task_manager.task_result import TaskResult


@dataclass
class Task:

    name: str

    callback: callable

    priority: int = 5

    state: TaskState = TaskState.PENDING

    id: str = field(default_factory=lambda: str(uuid4()))

    created: float = field(default_factory=time.time)

    started: float = 0.0

    finished: float = 0.0

    progress: float = 0.0

    result: TaskResult = field(default_factory=TaskResult)
