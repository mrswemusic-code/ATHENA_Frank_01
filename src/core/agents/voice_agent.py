from src.core.agents.base_agent import BaseAgent
from src.core.logger.logger import AthenaLogger


class VoiceAgent(BaseAgent):

    NAME = "voice"

    def __init__(self, kernel=None):

        super().__init__(
            self.NAME,
            kernel
        )

    def capabilities(self):

        return [

            "voice",

            "listen",

            "speech",

            "tts"

        ]

    def execute(self, task):

        AthenaLogger.info(
            f"[VOICE AGENT] Executing: {task.name}"
        )

        action = task.action

        payload = getattr(
            task,
            "payload",
            {}
        ) or {}

        #
        # Placeholder para el futuro Voice Engine
        #

        if action == "listen":

            return {

                "status": "not_implemented",

                "message": "Voice listening engine not available yet."

            }

        if action == "speech":

            return {

                "status": "not_implemented",

                "message": "Speech recognition engine not available yet."

            }

        if action == "tts":

            return {

                "status": "not_implemented",

                "message": "Text-to-Speech engine not available yet."

            }

        if action == "voice":

            return {

                "status": "ready",

                "message": "Voice Agent initialized and waiting for Voice Core."

            }

        return {

            "error":

            f"Unsupported voice action: {action}"

        }
