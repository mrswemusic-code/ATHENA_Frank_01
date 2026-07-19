from src.core.logger.logger import AthenaLogger


AGENT_CAPABILITIES = {

    "system":[
        "status",
        "hardware",
        "files",
        "applications",
        "terminal"
    ],

    "memory":[
        "memory",
        "remember",
        "recall",
        "search",
        "search_memory"
    ],

    "voice":[
        "voice",
        "listen",
        "speech",
        "tts"
    ],

    "internet":[
        "internet",
        "search_web",
        "news",
        "research"
    ],

    "music":[
        "music",
        "spotify",
        "playlist"
    ],

    "coding":[
        "coding",
        "code",
        "debug",
        "project"
    ],

    "vision":[
        "vision",
        "image",
        "camera",
        "analysis"
    ]

}


class CapabilityMatrix:


    def __init__(self):

        self.matrix = AGENT_CAPABILITIES

        AthenaLogger.info(
            "[ROUTER] Capability Matrix loaded"
        )


    def find_agent(self,intent):

        intent=intent.lower()

        for agent,capabilities in self.matrix.items():

            if intent in capabilities:

                return agent

        return "system"

