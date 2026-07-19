from src.core.logger.logger import AthenaLogger
from datetime import datetime


class StateEngine:


    def __init__(self):

        self.state = {}

        AthenaLogger.info(
            "STATE ENGINE INITIALIZED"
        )


    def update(self, data):

        self.state.update(data)

        self.state["timestamp"] = (
            datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S")
        )


    def get(self, key):

        return self.state.get(
            key,
            None
        )


    def snapshot(self):

        return self.state.copy()


    def report(self):

        AthenaLogger.info(
            "========== STATE REPORT =========="
        )


        for key,value in self.state.items():

            AthenaLogger.info(
                f"{key}: {value}"
            )


        AthenaLogger.info(
            "=================================="
        )
