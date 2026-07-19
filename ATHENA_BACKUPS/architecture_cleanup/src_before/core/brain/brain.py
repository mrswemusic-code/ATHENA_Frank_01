from src.core.logger.logger import AthenaLogger

from src.core.brain.intent_classifier import IntentClassifier
from src.core.planner.planner import Planner
from src.core.brain.context_manager import BrainContextManager

from src.core.response.context import ResponseContext



class AthenaBrain:


    def __init__(
        self,
        kernel
    ):


        self.kernel = kernel


        self.classifier = IntentClassifier()


        self.planner = Planner()


        self.context = BrainContextManager()


        self.response_context = ResponseContext()



        self.state = {


            "state":
            "IDLE",


            "intent":
            None,


            "history":
            []


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



        memory = self.kernel.get(
            "memory"
        )


        context = self.kernel.get(
            "context"
        )


        cognition = self.kernel.get(
            "cognition"
        )



        if memory:


            previous = memory.search(
                text
            )


            if previous:


                AthenaLogger.info(

                    "[BRAIN] Memory context found"

                )



        intent = self.classifier.classify(
            text
        )



        AthenaLogger.info(

            f"[BRAIN] Intent -> {intent.name}"

        )



        language = "es"



        if intent.payload:


            language = intent.payload.get(

                "language",

                "es"

            )



        #
        # RESPONSE CONTEXT UPDATE
        #

        self.response_context.update(

            intent=intent.name,

            language=language,

            mode="assistant",

            confidence=getattr(

                intent,

                "confidence",

                1.0

            ),

            metadata={


                "input":
                text,


                "source":
                "brain"

            }

        )



        self.state["intent"] = intent.name



        if context:


            context.conversation.add(

                "user",

                text,

                intent.name,

                language

            )


            context.state.update(

                state="THINKING",

                intent=intent.name

            )



        cognition_result = None



        if cognition:


            cognition_result = cognition.think(

                intent.name,

                {


                    "input":
                    text,


                    "language":
                    language


                }

            )



            AthenaLogger.info(

                "[COGNITION] Reasoning complete"

            )



        plan = self.planner.create_plan(

            intent.name,

            intent.payload

        )



        AthenaLogger.info(

            f"[PLANNER] Plan -> {plan.name}"

        )



        if context:


            context.state.update(

                plan=plan.name

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



        #
        # SEND RESPONSE CONTEXT
        #

        if response_engine:


            response_engine.context = self.response_context



        response = response_engine.generate(

            result

        )



        if memory:



            memory.remember(

                key=f"conversation_{len(self.state['history'])}",


                value={


                    "input":
                    text,


                    "intent":
                    intent.name,


                    "reasoning":
                    cognition_result,


                    "response":
                    response,


                    "context":

                    self.response_context.__dict__


                },


                category="conversation",


                persistent=True

            )



        self.context.update(

            text,

            intent.name,

            language,

            response

        )



        self.state["history"].append(

            {


                "input":
                text,


                "intent":
                intent.name,


                "response":
                response


            }

        )



        if context:


            context.conversation.add(

                "assistant",

                response,

                intent.name,

                language

            )


            context.state.update(

                state="READY"

            )



        self.state["state"] = "READY"



        return response
