from src.core.system.system_monitor import SystemMonitor


class SystemState:


    def __init__(self):

        self.monitor = SystemMonitor()

        self.data = {

            "cpu": 0,
            "ram": 0,
            "disk": 0

        }



    def update(self, data):

        if "cpu" in data:
            self.data["cpu"] = data["cpu"]


        if "ram" in data:
            self.data["ram"] = data["ram"]


        if "disk" in data:
            self.data["disk"] = data["disk"]



    def refresh(self):

        self.data = {

            "cpu":
                self.monitor.cpu(),


            "ram":
                self.monitor.ram(),


            "disk":
                self.monitor.disk()

        }



    def get(self):

        return self.data
