from dataclasses import dataclass
from datetime import datetime


@dataclass
class AthenaMessage:

    source: str

    target: str

    topic: str

    payload: dict


    def timestamp(self):

        return datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
