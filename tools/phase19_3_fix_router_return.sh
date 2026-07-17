#!/bin/bash

set -e


python3 << 'PY'

from pathlib import Path


file = Path(
"src/core/router/executive_router.py"
)


data = file.read_text()


data = data.replace(

'''            return selected''',

'''            return agent'''

)


file.write_text(data)


PY


echo "Router now returns agent instance."

