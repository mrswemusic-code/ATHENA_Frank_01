from src.services.core.service_manager import ServiceManager
from src.services.system.hardware_service import HardwareService

from src.core.logger.logger import AthenaLogger
from src.core.memory.memory_engine import MemoryEngine
from src.core.events.event_bus import EventBus
from src.core.scheduler.scheduler import Scheduler
from src.core.system.system_monitor import SystemMonitor
from src.core.hardware.hardware_manager import HardwareManager
from src.core.state.state_manager import StateManager


class AthenaApplication:


    def __init__(self):

        AthenaLogger.info(
            "Initializing ATHENA Core..."
        )


        # ==========================
        # CORE SYSTEMS
        # ==========================

        self.memory = MemoryEngine()

        self.events = EventBus()

        self.scheduler = Scheduler()

        self.monitor = SystemMonitor()

        self.hardware = HardwareManager()

        self.state = StateManager()



        # ==========================
        # SERVICE LAYER
        # ==========================

        self.services = ServiceManager()


        self.services.register(
            HardwareService()
        )


        AthenaLogger.info(
            "ATHENA Core initialized."
        )



    def boot(self):


        AthenaLogger.info(
            "Boot sequence started."
        )


        # START SERVICES

        self.services.start_all()



        # ==========================
        # STATE ENGINE SNAPSHOT
        # ==========================

        snapshot = self.state.snapshot()



        system = snapshot["system"]

        hardware = snapshot["hardware"]



        cpu = system["cpu"]

        ram = system["ram"]

        disk = system["disk"]


        temperature = hardware["temperature"]

        fan = hardware["fan"]

        battery = hardware["battery"]



        # ==========================
        # ATHENA STATUS OUTPUT
        # ==========================

        AthenaLogger.info(
            "========== ATHENA STATE =========="
        )


        AthenaLogger.info(
            f"CPU : {cpu}%"
        )


        AthenaLogger.info(
            f"RAM : {ram}%"
        )


        AthenaLogger.info(
            f"DISK: {disk}%"
        )


        AthenaLogger.info(
            f"TEMP: {temperature}°C"
        )


        AthenaLogger.info(
            f"FAN : {fan}"
        )


        AthenaLogger.info(
            f"BAT : {battery}"
        )


        AthenaLogger.info(
            "STATE ENGINE ONLINE"
        )


        AthenaLogger.info(
            "MEMORY ENGINE ONLINE"
        )


        AthenaLogger.info(
            "SERVICE LAYER ONLINE"
        )


        AthenaLogger.info(
            "=================================="
        )


        AthenaLogger.info(
            "ATHENA READY"
        )
