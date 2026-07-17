#!/bin/bash

set -e


FILE="src/core/agents/base_agent.py"


cp "$FILE" \
"ATHENA_BACKUPS/phase19_base_agent_before.py" 2>/dev/null || true



cat > "$FILE" << 'PY'

from src.core.logger.logger import AthenaLogger

from src.core.agents.core.agent_context import AgentContext

from src.core.agents.core.agent_result import AgentResult

from src.core.agents.core.capability import AgentCapability



class BaseAgent:


    """
    ATHENA Base Agent

    Foundation class for every ATHENA specialist agent.
    """


    def __init__(
        self,
        name
    ):

        self.name = name

        self.status = "OFFLINE"

        self.capabilities = []

        self.context = None


        AthenaLogger.info(
            f"[AGENT] {self.name} created"
        )



    def add_capability(
        self,
        name,
        description=""
    ):

        capability = AgentCapability(
            name,
            description
        )


        self.capabilities.append(
            capability
        )



    def boot(self):

        self.status = "ONLINE"


        AthenaLogger.info(
            f"[AGENT] {self.name} ONLINE"
        )



    def shutdown(self):

        self.status = "OFFLINE"


        AthenaLogger.info(
            f"[AGENT] {self.name} OFFLINE"
        )



    def can_handle(
        self,
        task
    ):

        for capability in self.capabilities:

            if capability.name == task:

                return True


        return False



    def execute(
        self,
        action,
        context=None
    ):


        self.context = context


        return AgentResult(

            success=False,

            agent=self.name,

            action=action,

            message="Action not implemented"

        )



    def info(self):

        return {

            "name": self.name,

            "status": self.status,

            "capabilities":
            [
                c.name
                for c in self.capabilities
            ]

        }

PY



echo "BaseAgent upgraded."

