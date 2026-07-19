from src.core.logger.logger import AthenaLogger

from src.core.telemetry.metrics import TelemetryMetric

from src.core.telemetry.event_detector import EventDetector



class TelemetryManager:



    def __init__(
        self,
        event_bus=None
    ):


        self.metrics = {}


        self.event_bus = event_bus


        self.detector = EventDetector(

            event_bus

        )


        AthenaLogger.info(

            "Telemetry Engine initialized."

        )



    def update(
        self,
        name,
        value
    ):


        metric = TelemetryMetric.create(

            name,

            value

        )


        self.metrics[name] = metric



        self.detector.analyze(

            name,

            value

        )



    def get(
        self,
        name
    ):


        metric = self.metrics.get(

            name

        )


        if metric:

            return metric.value


        return None



    def snapshot(self):


        return {


            name:
            {

                "value": metric.value,

                "time": metric.timestamp

            }


            for name, metric in self.metrics.items()

        }



    def events(self):

        return self.detector.history()
