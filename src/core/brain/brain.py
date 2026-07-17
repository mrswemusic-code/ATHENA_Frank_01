from src.core.logger.logger import AthenaLogger

from src.core.brain.intent_classifier import IntentClassifier

from src.core.planner.planner import Planner

from src.core.brain.context_manager import BrainContextManager



class AthenaBrain:



    def __init__(

        self,

        kernel

    ):


        self.kernel = kernel


        self.classifier = IntentClassifier()


        self.planner = Planner()


        self.context = BrainContextManager()



        self.state = {


            "state": "IDLE",

            "intent": None,

            "language": "es",

            "history": []

        }



        AthenaLogger.info(

            "ATHENA Brain initialized."

        )



    def think(

        self,

        text

    ):



        AthenaLogger.info(

            f"[BRAIN] Input -> {text}"

        )



        intent = self.classifier.classify(

            text

        )



        AthenaLogger.info(

            f"[BRAIN] Intent -> {intent.name}"

        )



        language = "es"



        if hasattr(

            intent,

            "payload"

        ):


            language = intent.payload.get(

                "language",

                "es"

            )



        self.state["intent"] = intent.name


        self.state["language"] = language



        self.context.update(

            text,

            intent.name,

            language

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


        result = execution.execute_plan(

            plan

        )



        response_engine = self.kernel.get(

            "response"

        )


        response = response_engine.generate(

            result

        )



        self.state["history"].append(

            {

                "input":

                    text,


                "intent":

                    intent.name,


                "language":

                    language,


                "response":

                    response

            }

        )



        self.state["state"] = "READY"



        return response



    def snapshot(self):


        return {


            "state":

                self.state,


            "context":

                self.context.snapshot()

        }
