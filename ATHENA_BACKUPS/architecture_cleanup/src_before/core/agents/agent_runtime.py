from src.core.logger.logger import AthenaLogger

from src.core.agents.agent_registry import AgentRegistry
from src.core.agents.agent_factory import AgentFactory



class AgentRuntime:


    def __init__(self, kernel=None):

        self.kernel = kernel

        self.registry = AgentRegistry()



    def boot(self):

        AthenaLogger.info(
            "[AGENTS] Loading Agent Runtime..."
        )


        for name in AgentFactory.agents:

            agent = AgentFactory.create(
                name,
                self.kernel
            )

            self.registry.register(
                agent
            )


        AthenaLogger.info(
            f"[AGENTS] {len(self.registry.all())} agents online"
        )



    def resolve(self, intent):

        for agent in self.registry.all().values():

            if agent.can_handle(intent):

                return agent


        return None



    def get(self,name):

        return self.registry.get(name)
