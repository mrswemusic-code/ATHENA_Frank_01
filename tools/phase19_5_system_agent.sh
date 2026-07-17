#!/bin/bash

set -e


cat > src/core/agents/system_agent.py << 'PY'


from src.core.agents.base_agent import BaseAgent
from src.core.logger.logger import AthenaLogger


import psutil



class SystemAgent(BaseAgent):


    def __init__(
        self,
        kernel=None
    ):

        super().__init__(
            "system"
        )

        self.kernel = kernel



    def boot(self):

        super().boot()



    def capabilities(self):

        return [

            "status",
            "system",
            "hardware",
            "monitor"

        ]



    def execute(
        self,
        task
    ):


        intent = getattr(
            task,
            "intent",
            "status"
        )


        AthenaLogger.info(
            f"[SYSTEM AGENT] Executing {intent}"
        )



        if intent in self.capabilities():


            return self.system_status()



        return {

            "error":
            "Unsupported system task"

        }



    def system_status(self):


        cpu = psutil.cpu_percent()


        memory = psutil.virtual_memory()


        disk = psutil.disk_usage("/")


        result = {


            "agent":
            self.name,


            "cpu":
            cpu,


            "ram":
            memory.percent,


            "disk":
            disk.percent,


            "temperature":
            self.temperature()


        }



        AthenaLogger.info(
            "[SYSTEM AGENT] Status collected"
        )


        return result



    def temperature(self):


        try:

            temps = psutil.sensors_temperatures()


            for name in temps:

                if temps[name]:

                    return temps[name][0].current


        except:

            pass



        return None


PY


echo "System Agent upgraded."

