#!/bin/bash

set -e

FILE="/opt/athena/system/src/core/kernel/kernel.py"

cp "$FILE" "/opt/athena/system/ATHENA_BACKUPS/phase18/kernel_before_agents.py"


python3 << 'PY'

from pathlib import Path

file = Path(
"/opt/athena/system/src/core/kernel/kernel.py"
)

data = file.read_text()


# Add import

old = """
from src.services.system.hardware_service import HardwareService
"""


new = """
from src.services.system.hardware_service import HardwareService

from src.core.agents.agent_runtime import AgentRuntime
"""


data = data.replace(old,new)


# Add variable

old = """
        self.loop = None
"""


new = """
        self.loop = None


        # =========================
        # AGENT RUNTIME
        # =========================

        self.agents = None
"""


data = data.replace(old,new)



# Add initialization after services

old = """
        self.services.register(

            HardwareService()

        )
"""


new = """
        self.services.register(

            HardwareService()

        )


        # =========================
        # AGENTS
        # =========================

        self.agents = AgentRuntime(
            self
        )

        self.agents.boot()
"""


data = data.replace(old,new)



# Register

old = """
        self.registry.register(

            "services",

            self.services

        )
"""


new = """
        self.registry.register(

            "services",

            self.services

        )


        self.registry.register(

            "agents",

            self.agents

        )
"""


data = data.replace(old,new)



file.write_text(data)

PY


echo "Kernel Agent Runtime integrated."
