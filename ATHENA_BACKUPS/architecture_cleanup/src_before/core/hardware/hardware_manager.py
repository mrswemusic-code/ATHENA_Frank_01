from src.modules.sensors.temperature import TemperatureSensor
from src.modules.sensors.battery import BatterySensor
from src.modules.sensors.fans import FanSensor


class HardwareManager:

    def __init__(self):

        self.temp = TemperatureSensor()
        self.battery = BatterySensor()
        self.fan = FanSensor()
