from src.core.logger.logger import AthenaLogger
from src.core.execution.execution_result import ExecutionResult


class ExecutionEngine:

    def __init__(self, kernel):

        self.kernel = kernel

        AthenaLogger.info(
            "Execution Engine initialized."
        )

    def execute_plan(self, plan):

        task_manager = self.kernel.get(
            "tasks"
        )

        if not task_manager:

            AthenaLogger.warning(
                "[EXECUTION] Task Manager unavailable"
            )

            return self._execute_direct(plan)

        AthenaLogger.info(
            "[EXECUTION] Executing plan"
        )

        for task in plan.tasks:

            task.callback = (
                lambda t=task:
                self._execute_task(t)
            )

            task_manager.submit(task)

        results = []

        while task_manager.pending() > 0:

            executed = task_manager.execute_next()

            if executed:

                results.append(
                    executed.result
                )

        return ExecutionResult(

            success=True,

            result=results,

            executed_tasks=len(results)

        )

    def _execute_task(self, task):

        router = self.kernel.get(
            "router"
        )

        agent = router.select_agent(task)

        if agent:

            AthenaLogger.info(

                f"[EXECUTION] Agent -> {agent.name}"

            )

            return agent.execute(task)

        command_bus = self.kernel.get(
            "command_bus"
        )

        return command_bus.dispatch(
            task.action
        )

    def _execute_direct(self, plan):

        results = []

        for task in plan.tasks:

            results.append(

                self._execute_task(task)

            )

        return ExecutionResult(

            success=True,

            result=results,

            executed_tasks=len(results)

        )
