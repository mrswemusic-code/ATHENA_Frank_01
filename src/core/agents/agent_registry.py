from src.core.logger.logger import AthenaLogger


class AgentRegistry:


    def __init__(self):

        self.agents = {}



    def register(self, agent):

        self.agents[
            agent.name
        ] = agent


        AthenaLogger.info(
            f"[AGENT REGISTRY] {agent.name}"
        )



    def get(self, name):

        return self.agents.get(name)



    def all(self):

        return self.agents
