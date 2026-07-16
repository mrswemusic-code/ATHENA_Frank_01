from src.core.state.hardware_state import HardwareState
from src.core.state.system_state import SystemState


class StateManager:


    def __init__(self):

        self.hardware = HardwareState()

        self.system = SystemState()



    def update(self, data):

        """
        Actualiza el estado global de ATHENA.

        Recibe información del sistema y distribuye
        los datos a los módulos correspondientes.
        """

        if "system" in data:

            self.system.update(
                data["system"]
            )


        if "hardware" in data:

            self.hardware.update(
                data["hardware"]
            )



    def snapshot(self):

        return {

            "athena": {

                "status":
                    "ONLINE",

                "version":
                    "0.2-alpha"

            },


            "system":
                self.system.get(),


            "hardware":
                self.hardware.get()

        }
