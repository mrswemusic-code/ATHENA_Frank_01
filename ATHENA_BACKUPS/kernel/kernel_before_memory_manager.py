from src.core.cognition.cognitive_engine import CognitiveEngine
from src.core.logger.logger import AthenaLogger


from src.core.registry.registry import AthenaRegistry


from src.core.memory.memory_engine import MemoryEngine
from src.core.events.event_bus import EventBus
from src.core.scheduler.scheduler import Scheduler
from src.core.system.system_monitor import SystemMonitor
from src.core.hardware.hardware_manager import HardwareManager
from src.core.state.state_manager import StateManager
from src.core.runtime.runtime_manager import RuntimeManager

from src.core.loop.event_loop import EventLoop


from src.core.telemetry.telemetry_manager import TelemetryManager


from src.services.core.service_manager import ServiceManager
from src.services.system.hardware_service import HardwareService



class AthenaKernel:



    def __init__(self):


        AthenaLogger.info(
            "Loading ATHENA Kernel..."
        )


        self.registry = AthenaRegistry()


        self.booted = False



    def boot(self):


        if self.booted:

            return



        AthenaLogger.info(
            "Booting Kernel..."
        )



        #
        # CORE SYSTEMS
        #

        memory = MemoryEngine()

        events = EventBus()

        scheduler = Scheduler()

        monitor = SystemMonitor()

        hardware = HardwareManager()

        state = StateManager()

        runtime = RuntimeManager()

        loop = EventLoop(
            rate=1.0
        )


        telemetry = TelemetryManager()
        cognition = CognitiveEngine()


        #
        # SERVICES
        #

        services = ServiceManager()


        services.register(
            HardwareService()
        )



        #
        # REGISTRY
        #

        components = {


            "memory": memory,

            "events": events,

            "scheduler": scheduler,

            "monitor": monitor,

            "hardware": hardware,

            "state": state,

            "runtime": runtime,

            "loop": loop,

            "telemetry": telemetry,

            "cognition": cognition,

            "services": services

        }



        for name, component in components.items():


            self.registry.register(
                name,
                component
            )



        runtime.boot()



        self.booted = True



        AthenaLogger.info(
            "Kernel ONLINE."
        )



    def start(self):


        if not self.booted:

            self.boot()



        loop = self.registry.get(
            "loop"
        )


        loop.start()



        AthenaLogger.info(
            "Kernel LOOP ACTIVE."
        )



    def stop(self):


        loop = self.registry.get(
            "loop"
        )


        if loop:

            loop.stop()



        self.booted = False



        AthenaLogger.info(
            "Kernel STOPPED."
        )



    def get(
        self,
        component
    ):


        return self.registry.get(
            component
        )



    def status(self):


        return {


            "booted":
            self.booted,


            "components":
            self.registry.list()

        }
