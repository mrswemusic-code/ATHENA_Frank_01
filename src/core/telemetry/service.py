from src.core.logger.logger import AthenaLogger


class TelemetryService:


    def __init__(
        self,
        telemetry,
        event_bus
    ):

        self.telemetry = telemetry
        self.event_bus = event_bus


        AthenaLogger.info(
            "Telemetry Service ONLINE"
        )



    def update(self):


        snapshot = self.telemetry.snapshot()



        for name, data in snapshot.items():

            value = data["value"]


            if name == "temperature" and value > 90:

                self.event_bus.emit(
                    type(
                        "Event",
                        (),
                        {
                            "name":
                            "TEMPERATURE_WARNING",

                            "data":
                            {
                                "value": value
                            }
                        }
                    )()
                )


            if name == "cpu" and value > 90:

                self.event_bus.emit(
                    type(
                        "Event",
                        (),
                        {
                            "name":
                            "CPU_OVERLOAD",

                            "data":
                            {
                                "value": value
                            }
                        }
                    )()
                )
