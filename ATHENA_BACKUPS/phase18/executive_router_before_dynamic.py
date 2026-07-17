from src.core.logger.logger import AthenaLogger


class ExecutiveRouter:

    """
    ATHENA Executive Router

    Responsible for deciding which agent
    should execute a generated plan.

    Future versions will support:

    - SystemAgent
    - BrowserAgent
    - ResearchAgent
    - MemoryAgent
    - CodingAgent
    - MusicAgent
    - VisionAgent
    - CryptoAgent
    """

    def __init__(self):

        AthenaLogger.info(
            "Executive Router initialized."
        )

    def select_agent(self, plan):

        """
        Current implementation.

        Everything goes through the
        default SystemAgent.
        """

        AthenaLogger.info(
            "[ROUTER] Selected -> SystemAgent"
        )

        return "system"
