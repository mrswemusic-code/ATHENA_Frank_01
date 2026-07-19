from src.core.logger.logger import AthenaLogger

from src.core.cognition.reasoning_engine import ReasoningEngine
from src.core.cognition.decision_engine import DecisionEngine
from src.core.cognition.goal_manager import GoalManager
from src.core.cognition.attention_manager import AttentionManager
from src.core.cognition.priority_engine import PriorityEngine


class CognitionEngine:

    def __init__(self):

        self.reasoning = ReasoningEngine()

        self.decision = DecisionEngine()

        self.goals = GoalManager()

        self.attention = AttentionManager()

        self.priority = PriorityEngine()

        AthenaLogger.info(
            "Cognition Engine initialized."
        )


    def think(self, intent, context=None):

        reasoning = self.reasoning.analyze(

            intent,

            context

        )

        decision = self.decision.decide(

            reasoning

        )

        return {

            "reasoning": reasoning,

            "decision": decision

        }
