from abc import ABC

from src.core.logger.logger import AthenaLogger


class BaseAgent(ABC):
    """
    Base class for every ATHENA Agent.

    Every specialized agent must inherit from this class.
    """

    def __init__(self, name: str, kernel=None):

        self.name = name
        self.kernel = kernel

        self.online = False

        AthenaLogger.info(
            f"[AGENT] {self.name} created"
        )

    # --------------------------------------------------

    def boot(self):

        self.online = True

        AthenaLogger.info(
            f"[AGENT] {self.name} ONLINE"
        )

    # --------------------------------------------------

    def shutdown(self):

        self.online = False

        AthenaLogger.info(
            f"[AGENT] {self.name} OFFLINE"
        )

    # --------------------------------------------------

    def capabilities(self):

        """
        List of supported capabilities.

        Example:

        return [
            "status",
            "hardware",
            "files"
        ]
        """

        return []

    # --------------------------------------------------

    def can_handle(self, capability: str):

        return capability in self.capabilities()

    # --------------------------------------------------

    def execute(self, task):

        raise NotImplementedError(
            f"{self.name} must implement execute()"
        )

    # --------------------------------------------------

    def status(self):

        return {

            "name": self.name,

            "online": self.online,

            "capabilities": self.capabilities()

        }
