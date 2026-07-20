from src.core.logger.logger import AthenaLogger


class ExecutiveRouter:

    """
    Dynamic Router

    The router does not know
    any capability.

    It simply asks AgentRuntime
    which agent can execute
    the task.
    """

    def __init__(self, kernel=None):

        self.kernel = kernel

        AthenaLogger.info(
            "Executive Router initialized."
        )

    def select_agent(self, task):

        if not self.kernel:

            return None

        runtime = self.kernel.get(
            "agents"
        )

        if runtime is None:

            AthenaLogger.warning(
                "[ROUTER] Agent Runtime unavailable"
            )

            return None

        intent = getattr(
            task,
            "action",
            ""
        )

        agent = runtime.resolve(
            intent
        )

        if agent:

            AthenaLogger.info(

                f"[ROUTER] {intent} -> {agent.name}"

            )

            return agent

        AthenaLogger.warning(

            f"[ROUTER] No agent for '{intent}'"

        )

        return None
