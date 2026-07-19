from src.core.agents.base_agent import BaseAgent
from src.core.agents.core.agent_result import AgentResult
from src.core.logger.logger import AthenaLogger


class MemoryAgent(BaseAgent):

    def __init__(self, name="memory"):

        super().__init__(name)

        self.kernel = None


    def capabilities(self):

        return [

            "memory",
            "remember",
            "recall",
            "search_memory"

        ]


    def execute(self, task):

        memory = self.kernel.get("memory")

        action = task.action

        payload = task.payload or {}


        if action == "remember":

            AthenaLogger.info("[MEMORY AGENT] Remember")

            result = memory.remember(

                key=payload.get("key"),

                value=payload.get("value"),

                category="conversation",

                persistent=True

            )

            return AgentResult(

                success=True,
                agent=self.name,
                action="remember",
                message="Stored",
                data=result

            )


        if action == "recall":

            AthenaLogger.info("[MEMORY AGENT] Recall")

            result = memory.recall(

                payload.get("key")

            )

            return AgentResult(

                success=True,
                agent=self.name,
                action="recall",
                message="Recovered",
                data=result

            )


        if action == "search":

            AthenaLogger.info("[MEMORY AGENT] Search")

            result = memory.search(

                payload.get("text","")

            )

            return AgentResult(

                success=True,
                agent=self.name,
                action="search",
                message="Search complete",
                data=result

            )


        return AgentResult(

            success=False,
            agent=self.name,
            action=action,
            message="Unsupported action"

        )
