from src.core.logger.logger import AthenaLogger


class DecisionEngine:

    def __init__(self):

        AthenaLogger.info(
            "Decision Engine initialized."
        )


    def decide(self, reasoning):

        decision = {

            "execute": True,

            "action": reasoning["recommended_action"],

            "confidence": reasoning["confidence"]

        }

        return decision
