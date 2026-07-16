from src.core.logger.logger import AthenaLogger

from src.core.memory.memory_engine import MemoryEngine
from src.core.events.event_bus import EventBus
from src.core.scheduler.scheduler import Scheduler
from src.core.system.system_monitor import SystemMonitor
from src.core.hardware.hardware_manager import HardwareManager
from src.core.state.state_manager import StateManager
from src.core.runtime.runtime_manager import RuntimeManager
from src.core.registry.registry import AthenaRegistry

from src.services.core.service_manager import ServiceManager
from src.services.system.hardware_service import HardwareService


class AthenaKernel:

    def __init__(self):

        AthenaLogger.info(
            "Loading ATHENA Kernel..."
        )

        self.registry = AthenaRegistry()

        self.memory = None
        self.events = None
        self.scheduler = None
        self.monitor = None
        self.hardware = None
        self.state = None
        self.runtime = None
        self.services = None

        self.booted = False


    def boot(self):

        if self.booted:
            return

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

        # Register all components

        self.registry.register(
            "memory",
            self.memory
        )

        self.registry.register(
            "events",
            self.events
        )

        self.registry.register(
            "scheduler",
            self.scheduler
        )

        self.registry.register(
            "monitor",
            self.monitor
        )

        self.registry.register(
            "hardware",
            self.hardware
        )

        self.registry.register(
            "state",
            self.state
        )

        self.registry.register(
            "runtime",
            self.runtime
        )

        self.registry.register(
            "services",
            self.services
        )

        self.runtime.boot()

        self.booted = True

        AthenaLogger.info(
            "Kernel ONLINE."
        )


    def get(self, component):

        return self.registry.get(component)
