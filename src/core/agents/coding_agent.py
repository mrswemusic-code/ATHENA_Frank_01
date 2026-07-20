from src.core.agents.base_agent import BaseAgent


class CodingAgent(BaseAgent):

    def __init__(self, kernel=None):

        super().__init__(
            name="coding",
            kernel=kernel
        )

    def capabilities(self):

        return [

            "coding",
            "code",
            "python",
            "linux",
            "debug",
            "project",
            "terminal"

        ]

    def execute(self, task):

        payload = getattr(
            task,
            "payload",
            {}
        )

        action = getattr(
            task,
            "action",
            "coding"
        )

        return {

            "agent": self.name,

            "status": "not_implemented",

            "action": action,

            "payload": payload,

            "message": "Coding subsystem not implemented yet."

        }
