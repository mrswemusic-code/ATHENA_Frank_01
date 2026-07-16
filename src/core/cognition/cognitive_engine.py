from src.core.logger.logger import AthenaLogger


class CognitiveEngine:


    def __init__(self):

        self.decisions = []


        AthenaLogger.info(
            "Cognitive Engine initialized."
        )



    def analyze(
        self,
        telemetry
    ):


        decisions = []


        temperature = telemetry.get(
            "temperature"
        )


        cpu = telemetry.get(
            "cpu"
        )



        if temperature:


            if temperature >= 90:


                decision = {

                    "type":
                    "THERMAL_WARNING",

                    "severity":
                    "HIGH",

                    "message":
                    "CPU temperature critical"

                }


                decisions.append(
                    decision
                )



        if cpu:


            if cpu >= 90:


                decision = {

                    "type":
                    "CPU_WARNING",

                    "severity":
                    "HIGH",

                    "message":
                    "CPU usage critical"

                }


                decisions.append(
                    decision
                )



        self.decisions.extend(
            decisions
        )


        for decision in decisions:

            AthenaLogger.info(
                f"[COGNITION] {decision}"
            )



        return decisions



    def history(self):

        return self.decisions
