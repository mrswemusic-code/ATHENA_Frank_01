from src.services.core.service_manager import ServiceManager
from src.services.system.hardware_service import HardwareService

from src.core.logger.logger import AthenaLogger
from src.core.memory.memory_engine import MemoryEngine
from src.core.events.event_bus import EventBus
from src.core.scheduler.scheduler import Scheduler
from src.core.system.system_monitor import SystemMonitor
from src.core.hardware.hardware_manager import HardwareManager
from src.core.state.state_manager import StateManager
from src.core.runtime.runtime_manager import RuntimeManager


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

        self.runtime = RuntimeManager()



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



        # ==========================
        # START SERVICES
        # ==========================

        self.services.start_all()



        # ==========================
        # START RUNTIME ENGINE
        # ==========================

        self.runtime.boot()



        # ==========================
        # HARDWARE / SYSTEM SNAPSHOT
        # ==========================

        cpu = self.monitor.cpu()

        ram = self.monitor.ram()

        disk = self.monitor.disk()


        temperature = self.hardware.temp.cpu()

        fan = self.hardware.fan.rpm()

        battery = self.hardware.battery.level()



        # ==========================
        # UPDATE STATE ENGINE
        # ==========================

        self.state.hardware.get()

        self.state.system.get()



        # ==========================
        # SYSTEM LOG
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
            "=================================="
        )



        # ==========================
        # RUNTIME STATUS
        # ==========================

        runtime_status = self.runtime.status()


        AthenaLogger.info(
            "========== ATHENA RUNTIME =========="
        )


        AthenaLogger.info(
            f"STATUS : {runtime_status['status']}"
        )


        for component, state in runtime_status["components"].items():

            AthenaLogger.info(
                f"{component} : {state}"
            )



        AthenaLogger.info(
            "===================================="
        )



        AthenaLogger.info(
            "ATHENA READY"
        )
