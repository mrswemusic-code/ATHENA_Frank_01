from datetime import datetime


class HealthMonitor:


    def __init__(self):

        self.status = "INITIALIZING"

        self.components = {}

        self.metrics = {}



    def register(
        self,
        name,
        state
    ):

        self.components[name] = state



    def update_metrics(
        self,
        metrics
    ):

        self.metrics = metrics



    def check(self):

        failed = []


        for name, state in self.components.items():

            if state != "ONLINE":

                failed.append(name)



        if failed:

            self.status = "WARNING"

        else:

            self.status = "OPTIMAL"



        return {

            "time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "status":
                self.status,

            "components":
                self.components,

            "metrics":
                self.metrics,

            "issues":
                failed

        }
