#!/bin/bash

set -e


FILE="src/core/agents/agent_factory.py"


cp "$FILE" \
"ATHENA_BACKUPS/phase19_agent_factory_before.py" 2>/dev/null || true



python3 << 'PY'

from pathlib import Path


file = Path(
"src/core/agents/agent_factory.py"
)


data = file.read_text()



data = data.replace(
"agent.initialize()",
"agent.boot()"
)



file.write_text(data)

PY


echo "AgentFactory lifecycle updated."

