from dataclasses import dataclass
from typing import Callable



@dataclass
class AthenaCommand:


    name: str

    description: str

    callback: Callable
