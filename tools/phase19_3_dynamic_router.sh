#!/bin/bash

set -e


cat > src/core/router/executive_router.py << 'PY'

from src.core.logger.logger import AthenaLogger



class ExecutiveRouter:


    """
    ATHENA Executive Router

    Selects the correct specialist agent
    according to the plan intent.
    """



    def __init__(self, kernel=None):

        self.kernel = kernel

        AthenaLogger.info(
            "Executive Router initialized."
        )



    def select_agent(
        self,
        plan
    ):


        agents = None


        if self.kernel:

            agents = self.kernel.get(
                "agents"
            )


        if not agents:

            AthenaLogger.warning(
                "[ROUTER] Agents unavailable"
            )

            return None



        intent = getattr(
            plan,
            "intent",
            "system"
        )



        mapping = {


            "status":
                "system",


            "system":
                "system",


            "memory":
                "memory",


            "voice":
                "voice",


            "music":
                "music",


            "internet":
                "internet",


            "coding":
                "coding",


            "vision":
                "vision"


        }



        selected = mapping.get(
            intent,
            "system"
        )



        agent = agents.get(
            selected
        )


        if agent:


            AthenaLogger.info(
                f"[ROUTER] Selected -> {selected}"
            )

            return selected



        AthenaLogger.warning(
            "[ROUTER] No matching agent"
        )


        return None

PY


echo "Dynamic Router upgraded."

