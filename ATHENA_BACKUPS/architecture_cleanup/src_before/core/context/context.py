from dataclasses import dataclass, field

from datetime import datetime


@dataclass
class Context:

    last_command: str | None = None

    last_intent: str | None = None

    last_agent: str | None = None

    current_project: str | None = None

    current_workspace: str | None = None

    conversation: list = field(default_factory=list)

    updated: str = field(
        default_factory=lambda: datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )
