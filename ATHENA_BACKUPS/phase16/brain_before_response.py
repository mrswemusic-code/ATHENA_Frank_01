from src.core.logger.logger import AthenaLogger

from src.core.brain.intent_classifier import IntentClassifier

from src.core.planner.planner import Planner


class AthenaBrain:

    def __init__(self, kernel):

        self.kernel = kernel

        self.classifier = IntentClassifier()

        self.planner = Planner()

        AthenaLogger.info(
            "ATHENA Brain initialized."
        )


    def think(self, text):

        intent = self.classifier.classify(text)

        AthenaLogger.info(
            f"[BRAIN] Intent -> {intent.name}"
        )

        plan = self.planner.create_plan(
            intent.name
        )

        AthenaLogger.info(
            f"[BRAIN] Plan -> {plan.name}"
        )

        execution = self.kernel.get(
            "execution"
        )

        return execution.execute_plan(
            plan
        )
