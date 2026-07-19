from dataclasses import dataclass


@dataclass
class ExecutionResult:

    success: bool

    result: object = None

    error: str = ""

    executed_tasks: int = 0
