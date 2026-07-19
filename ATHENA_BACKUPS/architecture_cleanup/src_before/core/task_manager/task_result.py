from dataclasses import dataclass


@dataclass
class TaskResult:

    success: bool = False

    output: object = None

    error: str | None = None

    execution_time: float = 0.0
