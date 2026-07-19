class CognitiveState:

    def __init__(self):

        self.state = "IDLE"

        self.current_intent = None

        self.current_agent = None

        self.current_plan = None


    def update(
        self,
        state=None,
        intent=None,
        agent=None,
        plan=None
    ):

        if state is not None:
            self.state = state

        if intent is not None:
            self.current_intent = intent

        if agent is not None:
            self.current_agent = agent

        if plan is not None:
            self.current_plan = plan


    def snapshot(self):

        return {

            "state": self.state,

            "intent": self.current_intent,

            "agent": self.current_agent,

            "plan": self.current_plan

        }
