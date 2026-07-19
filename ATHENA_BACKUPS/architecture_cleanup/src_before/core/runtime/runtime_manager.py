from src.core.runtime.health_monitor import HealthMonitor
from src.core.runtime.diagnostics import Diagnostics

from src.core.logger.logger import AthenaLogger



class RuntimeManager:


    def __init__(self):

        self.health = HealthMonitor()

        self.diagnostics = Diagnostics()

        self.kernel = None



    def attach_kernel(
        self,
        kernel
    ):

        self.kernel = kernel



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


        AthenaLogger.info(
            "Runtime Manager ONLINE."
        )



    def heartbeat(self):


        if not self.kernel:

            return



        monitor = self.kernel.get(
            "monitor"
        )


        if monitor:


            metrics = monitor.summary()


            self.health.update_metrics(
                metrics
            )


            AthenaLogger.info(
                f"[RUNTIME] Health {metrics}"
            )



    def status(self):

        return self.health.check()



    def diagnostics_report(self):

        return self.diagnostics.run()
