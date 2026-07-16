from dataclasses import dataclass
from typing import Callable


@dataclass
class AthenaTask:

    name: str

    callback: Callable

    repeat: bool = False

    interval: float = 1.0
