#!/bin/bash

set -e


cp src/core/agents/agent_factory.py \
ATHENA_BACKUPS/phase19_agent_factory_old.py 2>/dev/null || true



cat > src/core/agents/agent_factory.py << 'PY'

from src.core.agents.system_agent import SystemAgent
from src.core.agents.memory_agent import MemoryAgent
from src.core.agents.voice_agent import VoiceAgent
from src.core.agents.internet_agent import InternetAgent
from src.core.agents.music_agent import MusicAgent
from src.core.agents.coding_agent import CodingAgent
from src.core.agents.vision_agent import VisionAgent


from src.core.logger.logger import AthenaLogger



class AgentFactory:


    """
    ATHENA Agent Factory

    Creates and boots specialist agents.
    """


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


        if name not in cls.agents:

            raise ValueError(
                f"Unknown agent: {name}"
            )


        agent_class = cls.agents[name]


        agent = agent_class(
            kernel
        )


        # New ATHENA lifecycle

        if hasattr(
            agent,
            "boot"
        ):

            agent.boot()


        else:

            AthenaLogger.warning(
                f"[AGENT] {name} has no boot method"
            )


        return agent

PY


echo "AgentFactory upgraded."

