from src.core.logger.logger import AthenaLogger

from src.core.memory.memory_engine import MemoryEngine
from src.core.events.event_bus import EventBus
from src.core.scheduler.scheduler import Scheduler
from src.core.system.system_monitor import SystemMonitor
from src.core.hardware.hardware_manager import HardwareManager
from src.core.state.state_manager import StateManager
from src.core.runtime.runtime_manager import RuntimeManager

from src.services.core.service_manager import ServiceManager
from src.services.system.hardware_service import HardwareService


class AthenaKernel:

    def __init__(self):

        AthenaLogger.info(
            "Loading ATHENA Kernel..."
        )

        self.memory = None
        self.events = None
        self.scheduler = None
        self.monitor = None
        self.hardware = None
        self.state = None
        self.runtime = None
        self.services = None

    def boot(self):

        AthenaLogger.info(
            "Booting Kernel..."
        )

        self.memory = MemoryEngine()

        self.events = EventBus()

        self.scheduler = Scheduler()

        self.monitor = SystemMonitor()

        self.hardware = HardwareManager()

        self.state = StateManager()

        self.runtime = RuntimeManager()

        self.services = ServiceManager()

        self.services.register(
            HardwareService()
        )

        self.runtime.boot()

        AthenaLogger.info(
            "Kernel ONLINE."
        )
