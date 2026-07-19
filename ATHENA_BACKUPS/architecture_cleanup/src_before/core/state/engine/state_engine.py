from datetime import datetime


class StateEngine:


    def __init__(self):

        self.state = {

            "athena": {

                "status": "BOOTING",
                "version": "0.2.0-alpha",
                "codename": "GENESIS"

            },


            "system": {

                "cpu": 0,
                "ram": 0,
                "disk": 0

            },


            "hardware": {

                "temperature": None,
                "fan": None,
                "battery": None

            },


            "runtime": {

                "started": datetime.now().isoformat()

            }

        }



    def update(self, section, key, value):

        if section in self.state:

            self.state[section][key] = value



    def get(self):

        return self.state



    def status(self):

        return self.state["athena"]["status"]



    def ready(self):

        self.state["athena"]["status"] = "READY"
