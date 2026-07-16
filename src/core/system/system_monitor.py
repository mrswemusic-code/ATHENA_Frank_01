import psutil


class SystemMonitor:

    def cpu(self):

        return psutil.cpu_percent(interval=1)

    def ram(self):

        return psutil.virtual_memory().percent

    def disk(self):

        return psutil.disk_usage("/").percent
