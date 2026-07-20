from src.core.agents.system_agent import SystemAgent
from src.core.agents.memory_agent import MemoryAgent
from src.core.agents.voice_agent import VoiceAgent
from src.core.agents.internet_agent import InternetAgent
from src.core.agents.music_agent import MusicAgent
from src.core.agents.coding_agent import CodingAgent
from src.core.agents.vision_agent import VisionAgent


class AgentFactory:
    """
    Central registry of all built-in ATHENA agents.

    Future versions will discover external plugins
    automatically.
    """

    _registry = {

        "system": SystemAgent,

        "memory": MemoryAgent,

        "voice": VoiceAgent,

        "internet": InternetAgent,

        "music": MusicAgent,

        "coding": CodingAgent,

        "vision": VisionAgent,

    }

    @classmethod
    def names(cls):

        return tuple(cls._registry.keys())

    @classmethod
    def exists(cls, name):

        return name in cls._registry

    @classmethod
    def create(cls, name, kernel=None):

        if name not in cls._registry:

            raise ValueError(
                f"Unknown agent: {name}"
            )

        agent = cls._registry[name](kernel)

        agent.boot()

        return agent
