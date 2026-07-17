#!/bin/bash

set -e


cat > src/core/agents/base_agent.py << 'PY'


from src.core.logger.logger import AthenaLogger



class BaseAgent:


    def __init__(
        self,
        name
    ):

        self.name = name

        self.kernel = None

        self.online = False


        AthenaLogger.info(
            f"[AGENT] {self.name} created"
        )



    def boot(self):

        self.online = True


        AthenaLogger.info(
            f"[AGENT] {self.name} ONLINE"
        )



    def capabilities(self):

        return []



    def can_handle(
        self,
        intent
    ):

        return intent in self.capabilities()



    def execute(
        self,
        task
    ):

        AthenaLogger.warning(
            f"{self.name} has no executor"
        )


        return None



    def status(self):

        return {

            "name": self.name,

            "online": self.online,

            "capabilities":
                self.capabilities()

        }

PY


echo "Base Agent Interface installed."

