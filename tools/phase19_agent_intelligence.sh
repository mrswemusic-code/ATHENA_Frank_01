#!/bin/bash

set -e


mkdir -p src/core/agents/core


cat > src/core/agents/core/__init__.py << 'PY'
PY


cat > src/core/agents/core/agent_context.py << 'PY'

class AgentContext:

    def __init__(
        self,
        task=None,
        user=None,
        memory=None,
        state=None
    ):

        self.task = task
        self.user = user
        self.memory = memory
        self.state = state

PY



cat > src/core/agents/core/agent_result.py << 'PY'

class AgentResult:

    def __init__(
        self,
        success,
        agent,
        action,
        data=None,
        message=""
    ):

        self.success = success
        self.agent = agent
        self.action = action
        self.data = data
        self.message = message



    def to_dict(self):

        return {

            "success": self.success,
            "agent": self.agent,
            "action": self.action,
            "data": self.data,
            "message": self.message

        }

PY



cat > src/core/agents/core/capability.py << 'PY'

class AgentCapability:


    def __init__(
        self,
        name,
        description=""
    ):

        self.name = name
        self.description = description

PY



echo "Phase 19 Agent Intelligence base created."

