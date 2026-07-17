#!/bin/bash

set -e

ROOT="/opt/athena/system/src/core/agents"

echo "Installing ATHENA Agent Core..."

cat > "$ROOT/base_agent.py" << 'PY'
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
PY


cat > "$ROOT/system_agent.py" << 'PY'
from src.core.agents.base_agent import BaseAgent


class SystemAgent(BaseAgent):

    name = "system"

    description = "System monitoring agent"

    skills = [
        "status",
        "hardware",
        "monitor"
    ]


    def execute(self, task):

        if self.kernel:

            command = self.kernel.get(
                "commands"
            )

            return command.execute(
                "status"
            )

        return "System unavailable"
PY


cat > "$ROOT/memory_agent.py" << 'PY'
from src.core.agents.base_agent import BaseAgent


class MemoryAgent(BaseAgent):

    name = "memory"

    skills = [
        "memory"
    ]


    def execute(self, task):

        return "Memory agent online"
PY


cat > "$ROOT/voice_agent.py" << 'PY'
from src.core.agents.base_agent import BaseAgent


class VoiceAgent(BaseAgent):

    name = "voice"

    skills = [
        "voice"
    ]
PY


cat > "$ROOT/internet_agent.py" << 'PY'
from src.core.agents.base_agent import BaseAgent


class InternetAgent(BaseAgent):

    name = "internet"

    skills = [
        "search",
        "internet"
    ]
PY


cat > "$ROOT/music_agent.py" << 'PY'
from src.core.agents.base_agent import BaseAgent


class MusicAgent(BaseAgent):

    name = "music"

    skills = [
        "music"
    ]
PY


cat > "$ROOT/coding_agent.py" << 'PY'
from src.core.agents.base_agent import BaseAgent


class CodingAgent(BaseAgent):

    name = "coding"

    skills = [
        "code"
    ]
PY


cat > "$ROOT/vision_agent.py" << 'PY'
from src.core.agents.base_agent import BaseAgent


class VisionAgent(BaseAgent):

    name = "vision"

    skills = [
        "vision"
    ]
PY


cat > "$ROOT/agent_registry.py" << 'PY'
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
PY


cat > "$ROOT/agent_factory.py" << 'PY'
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
    def create(cls, name, kernel=None):

        agent = cls.agents[name](
            kernel
        )

        agent.initialize()

        return agent
PY


echo "Agent Core installed."
