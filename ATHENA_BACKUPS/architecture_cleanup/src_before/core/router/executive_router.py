from src.core.logger.logger import AthenaLogger
from src.core.router.capability_matrix import CapabilityMatrix



class ExecutiveRouter:


    """
    ATHENA Executive Router

    Dynamic agent selection using
    capability matching.
    """



    def __init__(self, kernel=None):

        self.kernel = kernel

        self.capabilities = CapabilityMatrix()


        AthenaLogger.info(
            "Executive Router initialized."
        )



    def select_agent(
        self,
        plan
    ):


        agents = None


        if self.kernel:

            agents = self.kernel.get(
                "agents"
            )



        if not agents:

            AthenaLogger.warning(
                "[ROUTER] Agents unavailable"
            )

            return None



        intent = getattr(
            plan,
            "intent",
            "status"
        )



        selected = self.capabilities.find_agent(
            intent
        )


        if not selected:

            selected = "system"



        agent = agents.get(
            selected
        )



        if agent:


            AthenaLogger.info(
                f"[ROUTER] Selected -> {selected}"
            )


            return agent



        AthenaLogger.warning(
            "[ROUTER] No matching agent"
        )


        return None
