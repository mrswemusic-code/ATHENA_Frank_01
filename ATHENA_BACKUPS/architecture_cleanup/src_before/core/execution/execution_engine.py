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

            return self._execute_direct(
                plan
            )


        AthenaLogger.info(
            "[EXECUTION] Routing plan through Task Manager"
        )


        tasks = []


        for task in plan.tasks:


            athena_task = task_manager.submit(

                name=task.name,

                callback=lambda t=task: self._execute_task(t),

                priority=getattr(
                    task,
                    "priority",
                    5
                )

            )


            tasks.append(
                athena_task
            )


        results = []


        while task_manager.pending() > 0:


            executed = task_manager.execute_next()


            if executed:

                results.append(

                    executed.result.output

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


        agent = router.select_agent(
            task
        )


        if agent:

            AthenaLogger.info(
                f"[EXECUTION] Agent -> {agent.name}"
            )


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


        return {

            "task":
                task.name,

            "result":
                result

        }



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
