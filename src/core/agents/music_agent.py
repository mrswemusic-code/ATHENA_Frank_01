from src.core.agents.base_agent import BaseAgent


class MusicAgent(BaseAgent):

    def __init__(self, kernel=None):

        super().__init__(
            name="music",
            kernel=kernel
        )

    def capabilities(self):

        return [

            "music",
            "spotify",
            "playlist",
            "player"

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
            "music"
        )

        return {

            "agent": self.name,

            "status": "not_implemented",

            "action": action,

            "payload": payload,

            "message": "Music subsystem not implemented yet."

        }
