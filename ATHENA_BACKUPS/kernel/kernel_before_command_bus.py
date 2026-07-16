from src.core.commands.command_manager import CommandManager
from src.core.commands.command_loader import CommandLoader

from src.core.logger.logger import AthenaLogger
from src.core.commands.command_manager import CommandManager

# CORE SYSTEMS

from src.core.memory.memory_engine import MemoryEngine
from src.core.memory.manager.memory_manager import MemoryManager

from src.core.events.event_bus import EventBus

from src.core.scheduler.scheduler import Scheduler

from src.core.system.system_monitor import SystemMonitor

from src.core.hardware.hardware_manager import HardwareManager

from src.core.state.state_manager import StateManager

from src.core.runtime.runtime_manager import RuntimeManager

from src.core.registry.registry import AthenaRegistry

from src.core.loop.event_loop import EventLoop



# SERVICES

from src.services.core.service_manager import ServiceManager
from src.services.system.hardware_service import HardwareService



class AthenaKernel:



    def __init__(self):


        AthenaLogger.info(
            "Loading ATHENA Kernel..."
        )


        self.registry = AthenaRegistry()


        # =========================
        # CORE COMPONENTS
        # =========================


        self.memory = None

        self.memory_manager = None

        self.commands = None

        self.commands_loader = None

        self.events = None

        self.scheduler = None

        self.monitor = None

        self.hardware = None

        self.state = None

        self.runtime = None

        self.services = None

        self.loop = None



        self.booted = False




    def boot(self):


        if self.booted:

            return



        AthenaLogger.info(
            "Booting Kernel..."
        )



        # =========================
        # INITIALIZE SYSTEMS
        # =========================


        self.memory = MemoryEngine()


        self.memory_manager = MemoryManager()


        self.commands = CommandManager()


        self.command_loader = CommandLoader(
            self
        )

        self.events = EventBus()


        self.scheduler = Scheduler()


        self.monitor = SystemMonitor()


        self.hardware = HardwareManager()


        self.state = StateManager()


        self.runtime = RuntimeManager()


        self.services = ServiceManager()


        self.loop = EventLoop(
            rate=1.0
        )


        # =========================
        # SERVICES
        # =========================


        self.services.register(

            HardwareService()

        )


        # =========================
        # REGISTRY
        # =========================


        self.registry.register(

            "memory",

            self.memory

        )


        self.registry.register(

            "memory_manager",

            self.memory_manager

        )


        self.registry.register(

            "commands",

            self.commands

        )

        self.command_loader.load(
            self.commands
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


        self.registry.register(

            "loop",

            self.loop

        )





        # =========================
        # START RUNTIME
        # =========================


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
