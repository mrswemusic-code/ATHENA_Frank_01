from src.core.logger.logger import AthenaLogger



AGENT_CAPABILITIES = {


    "system": [
        "status",
        "hardware",
        "files",
        "applications",
        "terminal"
    ],


    "memory": [
        "remember",
        "recall",
        "search_memory"
    ],


    "voice": [
        "listen",
        "speech",
        "tts"
    ],


    "internet": [
        "search",
        "news",
        "research"
    ],


    "music": [
        "spotify",
        "playlist",
        "audio"
    ],


    "coding": [
        "code",
        "debug",
        "project"
    ],


    "vision": [
        "image",
        "camera",
        "analysis"
    ]

}




class CapabilityMatrix:


    """
    ATHENA Dynamic Capability Router

    Resolves user intent into
    the most suitable specialist agent.
    """



    def __init__(self):

        self.matrix = AGENT_CAPABILITIES


        AthenaLogger.info(
            "[ROUTER] Capability Matrix loaded"
        )



    def find_agent(
        self,
        intent
    ):


        intent = intent.lower()



        for agent, capabilities in self.matrix.items():


            if intent in capabilities:

                return agent



        return None
