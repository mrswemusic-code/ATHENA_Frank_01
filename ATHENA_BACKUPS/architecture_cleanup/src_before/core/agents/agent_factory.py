
from src.core.agents.system_agent import SystemAgent
from src.core.agents.memory_agent import MemoryAgent
from src.core.agents.voice_agent import VoiceAgent
from src.core.agents.internet_agent import InternetAgent
from src.core.agents.music_agent import MusicAgent
from src.core.agents.coding_agent import CodingAgent
from src.core.agents.vision_agent import VisionAgent


class AgentFactory:


    agents = {

        "system": SystemAgent,
        "memory": MemoryAgent,
        "voice": VoiceAgent,
        "internet": InternetAgent,
        "music": MusicAgent,
        "coding": CodingAgent,
        "vision": VisionAgent

    }



    @classmethod
    def create(
        cls,
        name,
        kernel=None
    ):


        agent_class = cls.agents[name]


        agent = agent_class(name)


        agent.kernel = kernel


        if hasattr(agent,"boot"):

            agent.boot()


        return agent

