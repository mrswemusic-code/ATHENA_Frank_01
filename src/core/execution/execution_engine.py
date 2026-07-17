from src.core.logger.logger import AthenaLogger



class ExecutionEngine:


    def __init__(self, kernel):

        self.kernel = kernel


        AthenaLogger.info(
            "Execution Engine initialized."
        )



    def execute_plan(self, plan):


        results = []


        router = self.kernel.get(
            "router"
        )


        agent = router.select_agent(
            plan
        )



        if agent:

            AthenaLogger.info(
                f"[EXECUTION] Agent -> {agent.name}"
            )

        else:

            AthenaLogger.warning(
                "[EXECUTION] No agent available"
            )



        for task in plan.tasks:


            AthenaLogger.info(
                f"[EXECUTION] {task.name}"
            )


            task.start()



            if agent:


                result = agent.execute(
                    task
                )


            else:


                command_bus = self.kernel.get(
                    "command_bus"
                )


                result = command_bus.dispatch(
                    task.action
                )



            task.complete()



            results.append({

                "agent":
                    agent.name if agent else "none",

                "task":
                    task.name,

                "result":
                    result

            })


        return results
