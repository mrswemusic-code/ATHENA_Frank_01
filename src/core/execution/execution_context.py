from dataclasses import dataclass


@dataclass
class ExecutionContext:

    kernel: object

    user: str = "Mr.Swe"

    workspace: str = "default"

    language: str = "es"

    session: str = "default"
