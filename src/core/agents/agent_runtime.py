from src.core.logger.logger import AthenaLogger

from src.core.agents.agent_registry import AgentRegistry
from src.core.agents.agent_factory import AgentFactory


class AgentRuntime:

    def __init__(self, kernel=None):

        self.kernel = kernel

        self.registry = AgentRegistry()

    def boot(self):

        AthenaLogger.info(
            "[AGENTS] Starting Runtime..."
        )

        loaded = 0

        for name in AgentFactory.names():

            agent = AgentFactory.create(
                name,
                self.kernel
            )

            self.registry.register(
                agent
            )

            loaded += 1

        AthenaLogger.info(
            f"[AGENTS] {loaded} agents ONLINE"
        )

    def get(self, name):

        return self.registry.get(name)

    def all(self):

        return self.registry.all()

    def resolve(self, capability):

        for agent in self.registry.all().values():

            if agent.can_handle(capability):

                return agent

        return None
