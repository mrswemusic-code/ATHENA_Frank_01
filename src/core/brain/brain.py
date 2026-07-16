from src.core.logger.logger import AthenaLogger

from src.core.brain.intents.router import IntentRouter

from src.core.brain.planner import Planner

from src.core.brain.response import ResponseGenerator


class AthenaBrain:


    def __init__(
        self,
        kernel
    ):

        self.kernel = kernel

        self.router = IntentRouter()

        self.planner = Planner()

        self.response = ResponseGenerator()


        AthenaLogger.info(
            "ATHENA Brain initialized."
        )


    def think(
        self,
        text
    ):

        intent = self.router.detect(text)

        plan = self.planner.create_plan(
            intent
        )


        if plan["intent"] == "status":

            result = self.kernel.get(
                "command_bus"
            ).dispatch(
                "status"
            )

        else:

            result = {

                "message":

                "Command not implemented."

            }


        return self.response.create(
            result
        )
