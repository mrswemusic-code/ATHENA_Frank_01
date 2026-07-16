from src.core.logger.logger import AthenaLogger

from src.core.telemetry.telemetry_events import TelemetryEvent



class EventDetector:



    def __init__(self):

        self.events = []



    def analyze(
        self,
        name,
        value
    ):


        event = None



        if name == "temperature":


            if value >= 95:

                event = TelemetryEvent.create(

                    "HIGH_TEMPERATURE",

                    "CRITICAL",

                    value

                )


            elif value >= 85:

                event = TelemetryEvent.create(

                    "TEMPERATURE_WARNING",

                    "WARNING",

                    value

                )



        if name == "cpu":


            if value >= 90:

                event = TelemetryEvent.create(

                    "CPU_OVERLOAD",

                    "WARNING",

                    value

                )



        if event:


            self.events.append(
                event
            )


            AthenaLogger.info(

                f"[TELEMETRY EVENT] {event.name}"

            )


        return event



    def history(self):


        return self.events
