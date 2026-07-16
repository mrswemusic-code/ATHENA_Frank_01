from src.core.runtime.health_monitor import HealthMonitor
from src.core.runtime.diagnostics import Diagnostics



class RuntimeManager:


    def __init__(self):

        self.health = HealthMonitor()

        self.diagnostics = Diagnostics()



    def boot(self):


        self.health.register(
            "CORE",
            "ONLINE"
        )


        self.health.register(
            "MEMORY",
            "ONLINE"
        )


        self.health.register(
            "EVENTS",
            "ONLINE"
        )


        self.health.register(
            "SERVICES",
            "ONLINE"
        )



    def status(self):

        return self.health.check()



    def diagnostics_report(self):

        return self.diagnostics.run()
