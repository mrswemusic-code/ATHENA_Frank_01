from dataclasses import dataclass
from datetime import datetime


@dataclass
class TelemetryMetric:

    name: str

    value: object

    timestamp: str



    @staticmethod
    def create(name, value):

        return TelemetryMetric(

            name=name,

            value=value,

            timestamp=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        )
