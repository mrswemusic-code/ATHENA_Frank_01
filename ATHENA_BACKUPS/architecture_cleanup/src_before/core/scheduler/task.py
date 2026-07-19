from dataclasses import dataclass, field
import time
from typing import Callable


@dataclass
class SchedulerTask:

    name: str

    callback: Callable

    interval: float = 1.0

    priority: int = 5

    enabled: bool = True

    repeat: bool = True

    last_run: float = 0.0

    next_run: float = field(default_factory=time.time)

    executions: int = 0
