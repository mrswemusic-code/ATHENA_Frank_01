from src.core.context.conversation import Conversation
from src.core.context.working_memory import WorkingMemory
from src.core.context.cognitive_state import CognitiveState


class ContextRouter:

    def __init__(self):

        self.conversation = Conversation()

        self.working = WorkingMemory()

        self.state = CognitiveState()


    def snapshot(self):

        return {

            "conversation":

                self.conversation.history(),

            "working":

                self.working.snapshot(),

            "state":

                self.state.snapshot()

        }
