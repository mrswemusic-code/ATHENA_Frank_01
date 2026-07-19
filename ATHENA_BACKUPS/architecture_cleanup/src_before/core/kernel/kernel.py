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

from src.core.context import ContextRouter
from src.core.cognition import CognitionEngine

from src.core.brain.brain import AthenaBrain
from src.core.executive.executive_loop import ExecutiveLoop
from src.core.loop.event_loop import EventLoop

from src.core.commands.command_manager import CommandManager
from src.core.commands.command_loader import CommandLoader
from src.core.commands.bus.command_bus import CommandBus

from src.core.execution.execution_engine import ExecutionEngine
from src.core.response.response_engine import ResponseEngine

from src.core.router.executive_router import ExecutiveRouter

from src.services.core.service_manager import ServiceManager
from src.services.system.hardware_service import HardwareService

from src.core.agents.agent_runtime import AgentRuntime

from src.core.task_manager.task_manager import TaskManager


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

        self.context = None
        self.cognition = None

        self.brain = None
        self.executive = None

        self.commands = None
        self.command_bus = None

        self.router = None
        self.execution = None
        self.response = None

        self.services = None
        self.agents = None
        self.loop = None

        self.tasks = None


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

        self.runtime.attach_kernel(
            self
        )

        self.context = ContextRouter()

        self.cognition = CognitionEngine()

        self.services = ServiceManager()

        self.services.register(
            HardwareService()
        )

        self.agents = AgentRuntime(
            self
        )

        self.agents.boot()

        self.commands = CommandManager()

        loader = CommandLoader(
            self
        )

        loader.load(
            self.commands
        )

        self.command_bus = CommandBus(
            self.commands
        )

        self.router = ExecutiveRouter(
            self
        )

        self.execution = ExecutionEngine(
            self
        )

        self.response = ResponseEngine()

        self.brain = AthenaBrain(
            self
        )

        self.executive = ExecutiveLoop(
            self
        )

        self.tasks = TaskManager()

        self.loop = EventLoop(
            kernel=self,
            rate=1.0
        )

        self.loop.register(
            self.runtime.heartbeat
        )

        self.loop.register(
            self.scheduler.run_pending
        )

        components = {

            "identity": self.identity,

            "memory": self.memory,

            "telemetry": self.telemetry,

            "events": self.events,

            "scheduler": self.scheduler,

            "tasks": self.tasks,

            "monitor": self.monitor,

            "hardware": self.hardware,

            "state": self.state,

            "runtime": self.runtime,

            "context": self.context,

            "cognition": self.cognition,

            "brain": self.brain,

            "executive": self.executive,

            "services": self.services,

            "agents": self.agents,

            "commands": self.commands,

            "command_bus": self.command_bus,

            "router": self.router,

            "execution": self.execution,

            "response": self.response,

            "loop": self.loop

        }

        for name, component in components.items():

            self.registry.register(
                name,
                component
            )

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

        return self.registry.get(
            component
        )
