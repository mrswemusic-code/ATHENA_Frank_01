#!/bin/bash

set -e


python3 << 'PY'

from pathlib import Path


file = Path(
"src/core/agents/agent_factory.py"
)


data = file.read_text()


data = data.replace(
"agent = agent_class()",
"agent = agent_class(name)"
)


file.write_text(data)


PY


echo "Factory name injection fixed."

