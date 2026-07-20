from src.core.agents.base_agent import BaseAgent
from src.core.logger.logger import AthenaLogger


class MemoryAgent(BaseAgent):

    NAME = "memory"

    def __init__(self, kernel=None):

        super().__init__(
            self.NAME,
            kernel
        )

    def capabilities(self):

        return [

            "memory",

            "remember",

            "recall",

            "search",

            "search_memory"

        ]

    def execute(self, task):

        AthenaLogger.info(
            f"[MEMORY AGENT] Executing: {task.name}"
        )

        memory = self.kernel.get(
            "memory"
        )

        if not memory:

            return {

                "error": "Memory Engine unavailable"

            }

        action = task.action

        payload = getattr(
            task,
            "payload",
            {}
        ) or {}

        if action == "remember":

            return memory.remember(

                key=payload.get("key"),

                value=payload.get("value"),

                category=payload.get(
                    "category",
                    "general"
                ),

                persistent=payload.get(
                    "persistent",
                    False
                )

            )

        if action == "recall":

            return memory.recall(

                payload.get("key")

            )

        if action in (

            "search",

            "search_memory",

            "memory"

        ):

            return memory.search(

                payload.get(

                    "text",

                    ""

                )

            )

        return {

            "error":

            f"Unsupported memory action: {action}"

        }
