from src.core.agents.base_agent import BaseAgent
from src.core.agents.core.agent_result import AgentResult
from src.core.logger.logger import AthenaLogger



class MemoryAgent(BaseAgent):


    def __init__(
        self,
        name="memory"
    ):

        super().__init__(
            name
        )



    def capabilities(
        self
    ):

        return [

            "memory",

            "remember",

            "recall"

        ]



    def execute(
        self,
        task
    ):


        action = getattr(
            task,
            "action",
            None
        )



        if action == "remember":


            AthenaLogger.info(
                "[MEMORY AGENT] Remember request"
            )


            return AgentResult(

                success=True,

                agent=self.name,

                action="remember",

                message="Memory stored",

                data=getattr(
                    task,
                    "payload",
                    {}

                )

            )



        if action == "recall":


            AthenaLogger.info(
                "[MEMORY AGENT] Recall request"
            )


            return AgentResult(

                success=True,

                agent=self.name,

                action="recall",

                message="Memory recalled",

                data=getattr(
                    task,
                    "payload",
                    {}

                )

            )



        return AgentResult(

            success=True,

            agent=self.name,

            action="memory",

            message="Memory agent online"

        )
