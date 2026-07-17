
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

