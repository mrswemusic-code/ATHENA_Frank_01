from src.core.logger.logger import AthenaLogger

from src.core.planner.plan import Plan
from src.core.planner.task import Task



class Planner:



    def __init__(self):

        AthenaLogger.info(
            "Planner initialized."
        )



    def create_plan(
        self,
        intent,
        payload=None
    ):


        plan = Plan(
            intent
        )


        payload = payload or {}



        if intent == "system":


            plan.add(

                Task(

                    name="Collect System Status",

                    action="status",

                    payload=payload

                )

            )



        elif intent == "memory":



            operation = payload.get(
                "operation"
            )



            if operation == "remember":


                plan.add(

                    Task(

                        name="Store Memory",

                        action="remember",

                        payload={

                            "key":
                                payload.get("key"),

                            "value":
                                payload.get("value"),

                            "language":
                                payload.get("language")

                        }

                    )

                )



            elif operation == "recall":


                plan.add(

                    Task(

                        name="Recall Memory",

                        action="recall",

                        payload={

                            "key":
                                payload.get("key"),

                            "language":
                                payload.get("language")

                        }

                    )

                )



            else:


                plan.add(

                    Task(

                        name="Memory Operation",

                        action="memory",

                        payload=payload

                    )

                )



        elif intent == "music":


            plan.add(

                Task(

                    name="Music Operation",

                    action="music",

                    payload=payload

                )

            )



        elif intent == "internet":


            plan.add(

                Task(

                    name="Internet Search",

                    action="search",

                    payload=payload

                )

            )



        elif intent == "coding":


            plan.add(

                Task(

                    name="Coding Assistance",

                    action="coding",

                    payload=payload

                )

            )



        elif intent == "voice":


            plan.add(

                Task(

                    name="Voice Operation",

                    action="voice",

                    payload=payload

                )

            )



        elif intent == "vision":


            plan.add(

                Task(

                    name="Vision Analysis",

                    action="vision",

                    payload=payload

                )

            )



        else:


            plan.add(

                Task(

                    name="Unknown Command",

                    action="unknown",

                    payload=payload

                )

            )



        AthenaLogger.info(

            f"[PLANNER] Plan created: {intent}"

        )


        return plan
