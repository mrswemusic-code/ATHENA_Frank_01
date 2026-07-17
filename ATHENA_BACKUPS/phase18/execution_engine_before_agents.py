from src.core.logger.logger import AthenaLogger


class ExecutionEngine:

    def __init__(self, kernel):

        self.kernel = kernel

        AthenaLogger.info(
            "Execution Engine initialized."
        )

    def execute_plan(self, plan):

        results = []

        command_bus = self.kernel.get(
            "command_bus"
        )

        router = self.kernel.get(
            "router"
        )

        agent = router.select_agent(
            plan
        )

        AthenaLogger.info(
            f"[EXECUTION] Agent -> {agent}"
        )

        for task in plan.tasks:

            AthenaLogger.info(
                f"[EXECUTION] {task.name}"
            )

            task.start()

            result = command_bus.dispatch(
                task.action
            )

            task.complete()

            results.append({

                "agent": agent,

                "task": task.name,

                "result": result

            })

        return results
