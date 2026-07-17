#!/bin/bash

set -e

FILE="/opt/athena/system/src/core/kernel/kernel.py"

cp "$FILE" \
"/opt/athena/system/ATHENA_BACKUPS/phase18/kernel_before_agents_registry.py"


python3 << 'PY'

from pathlib import Path


file = Path(
"/opt/athena/system/src/core/kernel/kernel.py"
)


data = file.read_text()



# Insert agent creation after services

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
        # AGENT RUNTIME
        # =========================

        self.agents = AgentRuntime(
            self
        )

        self.agents.boot()
"""


data = data.replace(old,new)



# Register agents

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


data=data.replace(old,new)



file.write_text(data)

PY


echo "Agent Runtime registered."
