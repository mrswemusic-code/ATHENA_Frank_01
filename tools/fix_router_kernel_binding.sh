#!/bin/bash

set -e

FILE="/opt/athena/system/src/core/kernel/kernel.py"

cp "$FILE" \
"/opt/athena/system/ATHENA_BACKUPS/phase18/kernel_before_router_binding.py"


python3 << 'PY'

from pathlib import Path

file = Path(
"/opt/athena/system/src/core/kernel/kernel.py"
)

data = file.read_text()


old = """
        self.router = ExecutiveRouter()
"""


new = """
        self.router = ExecutiveRouter(
            self
        )
"""


if old in data:

    data=data.replace(old,new)

else:

    print("Router creation pattern not found")



file.write_text(data)

PY


echo "Router Kernel binding fixed."
