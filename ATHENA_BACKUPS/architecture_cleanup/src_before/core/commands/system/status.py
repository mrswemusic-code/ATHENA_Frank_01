from src.core.logger.logger import AthenaLogger



class StatusCommand:



    def __init__(self, kernel):

        self.kernel = kernel




    def execute(self):


        monitor = self.kernel.get(
            "monitor"
        )


        hardware = self.kernel.get(
            "hardware"
        )


        runtime = self.kernel.get(
            "runtime"
        )



        status = {}



        status["cpu"] = (
            monitor.cpu()
        )


        status["ram"] = (
            monitor.ram()
        )


        status["disk"] = (
            monitor.disk()
        )



        status["temperature"] = (
            hardware.temp.cpu()
        )


        status["fan"] = (
            hardware.fan.rpm()
        )


        status["battery"] = (
            hardware.battery.level()
        )



        status["runtime"] = (
            runtime.status()
        )



        AthenaLogger.info(
            "[COMMAND] STATUS executed"
        )


        return status
