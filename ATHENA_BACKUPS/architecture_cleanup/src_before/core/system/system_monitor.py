import psutil

from src.core.logger.logger import AthenaLogger


class SystemMonitor:


    def __init__(self):

        AthenaLogger.info(
            "System Monitor initialized."
        )



    def cpu(self):

        return psutil.cpu_percent(
            interval=0.5
        )



    def ram(self):

        return psutil.virtual_memory().percent



    def disk(self):

        return psutil.disk_usage(
            "/"
        ).percent



    def summary(self):

        return {

            "cpu":
                self.cpu(),

            "ram":
                self.ram(),

            "disk":
                self.disk()

        }
