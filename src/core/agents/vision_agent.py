from src.core.agents.base_agent import BaseAgent


class VisionAgent(BaseAgent):

    def __init__(self, kernel=None):

        super().__init__(
            name="vision",
            kernel=kernel
        )

    def capabilities(self):

        return [

            "vision",
            "image",
            "camera",
            "ocr",
            "analysis"

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
            "vision"
        )

        return {

            "agent": self.name,

            "status": "not_implemented",

            "action": action,

            "payload": payload,

            "message": "Vision subsystem not implemented yet."

        }
