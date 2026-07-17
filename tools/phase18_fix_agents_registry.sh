#!/bin/bash

set -e

FILE="/opt/athena/system/src/core/kernel/kernel.py"

cp "$FILE" \
"/opt/athena/system/ATHENA_BACKUPS/phase18/kernel_before_agents_fix_final.py"


python3 << 'PY'

from pathlib import Path

file = Path(
"/opt/athena/system/src/core/kernel/kernel.py"
)

data = file.read_text()


# Insert Agent Runtime creation after HardwareService registration

target = """        self.services.register(
            HardwareService()
        )
"""


replacement = """        self.services.register(
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


if target in data:

    data = data.replace(
        target,
        replacement,
        1
    )

else:

    print("Service block not found")


# Insert registry entry after services registration

target2 = """        self.registry.register(
            "services",
            self.services
        )
"""


replacement2 = """        self.registry.register(
            "services",
            self.services
        )


        self.registry.register(
            "agents",
            self.agents
        )
"""


if target2 in data:

    data = data.replace(
        target2,
        replacement2,
        1
    )

else:

    print("Registry services block not found")


file.write_text(data)

PY


echo "Agent Runtime registry integration complete."
