from src.core.logger.logger import AthenaLogger

from src.core.registry.registry import AthenaRegistry

from src.core.identity.identity_manager import IdentityManager
from src.core.memory.memory_engine import MemoryEngine
from src.core.telemetry.telemetry_manager import TelemetryManager
from src.core.events.event_bus import EventBus
from src.core.scheduler.scheduler import Scheduler
from src.core.system.system_monitor import SystemMonitor
from src.core.hardware.hardware_manager import HardwareManager
from src.core.state.state_manager import StateManager
from src.core.runtime.runtime_manager import RuntimeManager
from src.core.loop.event_loop import EventLoop

from src.core.commands.command_manager import CommandManager
from src.core.commands.command_loader import CommandLoader
from src.core.commands.bus.command_bus import CommandBus

from src.core.execution.execution_engine import ExecutionEngine

from src.services.core.service_manager import ServiceManager
from src.services.system.hardware_service import HardwareService


class AthenaKernel:

    def __init__(self):

        AthenaLogger.info(
            "Loading ATHENA Kernel..."
        )

        self.registry = AthenaRegistry()

        self.booted = False

        self.identity = None
        self.memory = None
        self.telemetry = None
        self.events = None
        self.scheduler = None
        self.monitor = None
        self.hardware = None
        self.state = None
        self.runtime = None

        self.services = None

        self.loop = None

        self.commands = None
        self.command_bus = None

        self.execution = None

    def boot(self):

        if self.booted:
            return

        AthenaLogger.info(
            "Booting Kernel..."
        )

        self.identity = IdentityManager()

        self.memory = MemoryEngine()

        self.telemetry = TelemetryManager()

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

        self.commands = CommandManager()

        loader = CommandLoader(self)

        loader.load(self.commands)

        self.command_bus = CommandBus(
            self.commands
        )

        self.execution = ExecutionEngine(
            self
        )

        self.loop = EventLoop(
            rate=1.0
        )

        self.registry.register("identity", self.identity)
        self.registry.register("memory", self.memory)
        self.registry.register("telemetry", self.telemetry)
        self.registry.register("events", self.events)
        self.registry.register("scheduler", self.scheduler)
        self.registry.register("monitor", self.monitor)
        self.registry.register("hardware", self.hardware)
        self.registry.register("state", self.state)
        self.registry.register("runtime", self.runtime)
        self.registry.register("services", self.services)
        self.registry.register("commands", self.commands)
        self.registry.register("command_bus", self.command_bus)
        self.registry.register("execution", self.execution)
        self.registry.register("loop", self.loop)
        self.runtime.boot()

        self.booted = True

        AthenaLogger.info(
            "Kernel ONLINE."
        )

    def start(self):

        if not self.booted:
            self.boot()

        self.loop.start()

        AthenaLogger.info(
            "Kernel LOOP ACTIVE."
        )

    def stop(self):

        if self.loop:
            self.loop.stop()

        AthenaLogger.info(
            "Kernel STOPPED."
        )

    def get(self, component):

        return self.registry.get(component)
