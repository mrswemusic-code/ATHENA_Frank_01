
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

