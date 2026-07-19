from src.core.logger.logger import AthenaLogger

from src.core.telemetry.telemetry_events import TelemetryEvent

from src.core.events.event import Event



class EventDetector:


    def __init__(
        self,
        event_bus=None
    ):

        self.events = []

        self.event_bus = event_bus



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


            if self.event_bus:


                bus_event = Event(

                    event.name,

                    {

                        "severity": event.severity,

                        "value": event.value

                    }

                )


                self.event_bus.emit(
                    bus_event
                )



        return event



    def history(self):

        return self.events
