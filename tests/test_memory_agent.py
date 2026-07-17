from src.core.memory.memory_engine import MemoryEngine
from src.core.agents.memory_agent import MemoryAgent
from src.core.planner.task import Task



class KernelMock:


    def __init__(self):

        self.memory = MemoryEngine()


    def get(self,key):

        if key == "memory":

            return self.memory



kernel = KernelMock()


agent = MemoryAgent()

agent.kernel = kernel


agent.boot()



print("\nMEMORY AGENT TEST")
print("----------------")



remember_task = Task(

    name="Remember browser",

    action="remember",

    payload={

        "key":"browser",

        "value":"Brave",

        "category":"preference"

    }

)



print(

    agent.execute(

        remember_task

    )

)



recall_task = Task(

    name="Recall browser",

    action="recall",

    payload={

        "key":"browser"

    }

)



print(

    agent.execute(

        recall_task

    )

)
