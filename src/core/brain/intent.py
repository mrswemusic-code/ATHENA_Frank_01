from dataclasses import dataclass


@dataclass
class Intent:

    name: str

    confidence: float

    payload: dict
