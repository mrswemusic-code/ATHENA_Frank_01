#!/bin/bash

set -e

ROOT="/opt/athena/system"

echo ""
echo "========================================"
echo " ATHENA PHASE 18"
echo " Executive Agents Generator"
echo "========================================"
echo ""

mkdir -p "$ROOT/src/core/agents"

FILES=(
base_agent.py
system_agent.py
memory_agent.py
voice_agent.py
internet_agent.py
music_agent.py
coding_agent.py
vision_agent.py
agent_registry.py
agent_factory.py
)

for FILE in "${FILES[@]}"
do
    TARGET="$ROOT/src/core/agents/$FILE"

    if [ ! -f "$TARGET" ]; then
        touch "$TARGET"
        echo "[CREATED] $FILE"
    else
        echo "[EXISTS ] $FILE"
    fi
done

touch "$ROOT/src/core/agents/__init__.py"

mkdir -p "$ROOT/tests"

touch "$ROOT/tests/test_agents.py"

mkdir -p "$ROOT/docs"

touch "$ROOT/docs/PHASE18_EXECUTIVE_AGENTS.md"

mkdir -p "$ROOT/ATHENA_BACKUPS/phase18"

echo ""
echo "Phase 18 structure ready."
echo ""
