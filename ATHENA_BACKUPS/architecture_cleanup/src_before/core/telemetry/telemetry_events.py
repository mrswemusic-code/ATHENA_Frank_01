from dataclasses import dataclass
from datetime import datetime



@dataclass
class TelemetryEvent:


    name: str

    severity: str

    value: object

    timestamp: str



    @staticmethod
    def create(
        name,
        severity,
        value
    ):

        return TelemetryEvent(

            name=name,

            severity=severity,

            value=value,

            timestamp=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )
