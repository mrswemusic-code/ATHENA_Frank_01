from src.core.logger.logger import AthenaLogger


class BaseAgent:

    name = "base"
    description = "Generic ATHENA agent"
    skills = []

    def __init__(self, kernel=None):

        self.kernel = kernel
        self.active = False


    def initialize(self):

        self.active = True

        AthenaLogger.info(
            f"[AGENT] {self.name} initialized"
        )


    def can_handle(self, intent):

        return intent in self.skills


    def execute(self, task):

        raise NotImplementedError(
            "Agent must implement execute()"
        )


    def shutdown(self):

        self.active = False
