from src.core.hardware.hardware_manager import HardwareManager


class HardwareState:


    def __init__(self):

        self.hardware = HardwareManager()


        self.data = {

            "temperature": None,
            "fan": None,
            "battery": None

        }



    def update(self, data):


        if "temperature" in data:
            self.data["temperature"] = data["temperature"]


        if "fan" in data:
            self.data["fan"] = data["fan"]


        if "battery" in data:
            self.data["battery"] = data["battery"]



    def refresh(self):


        self.data = {


            "temperature":
                self.hardware.temp.cpu(),


            "fan":
                self.hardware.fan.rpm(),


            "battery":
                self.hardware.battery.level()


        }



    def get(self):

        return self.data
