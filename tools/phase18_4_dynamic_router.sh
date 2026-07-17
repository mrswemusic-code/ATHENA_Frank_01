#!/bin/bash

set -e

ROOT="/opt/athena/system"

mkdir -p "$ROOT/ATHENA_BACKUPS/phase18"

cp "$ROOT/src/core/router/executive_router.py" \
"$ROOT/ATHENA_BACKUPS/phase18/executive_router_before_dynamic.py"

cp "$ROOT/src/core/execution/execution_engine.py" \
"$ROOT/ATHENA_BACKUPS/phase18/execution_engine_before_agents.py"


cat > "$ROOT/src/core/router/executive_router.py" << 'PY'
from src.core.logger.logger import AthenaLogger



class ExecutiveRouter:


    def __init__(self, kernel=None):

        self.kernel = kernel

        AthenaLogger.info(
            "Executive Router initialized."
        )



    def select_agent(self, plan):


        intent = plan.name


        runtime = self.kernel.get(
            "agents"
        )


        if runtime:


            agent = runtime.resolve(
                intent
            )


            if agent:


                AthenaLogger.info(
                    f"[ROUTER] Selected -> {agent.name}"
                )


                return agent



        AthenaLogger.warning(
            "[ROUTER] No agent found"
        )


        return None
PY



cat > "$ROOT/src/core/execution/execution_engine.py" << 'PY'
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
PY


echo "Dynamic Router installed."
