from src.core.agents.base_agent import BaseAgent
from src.core.logger.logger import AthenaLogger


class SystemAgent(BaseAgent):

    NAME = "system"

    def __init__(self, kernel=None):

        super().__init__(
            self.NAME,
            kernel
        )

    def capabilities(self):

        return [

            "system",

            "status",

            "hardware",

            "files",

            "applications",

            "terminal"

        ]

    def execute(self, task):

        AthenaLogger.info(
            f"[SYSTEM AGENT] Executing: {task.name}"
        )

        command_bus = self.kernel.get(
            "command_bus"
        )

        if not command_bus:

            return {

                "error": "Command Bus unavailable"

            }

        return command_bus.dispatch(
            task.action
        )
