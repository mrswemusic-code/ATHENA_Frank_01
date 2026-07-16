from src.core.commands.command import AthenaCommand

from src.core.commands.system.status import StatusCommand




class CommandLoader:



    def __init__(
        self,
        kernel
    ):

        self.kernel = kernel



    def load(
        self,
        manager
    ):


        status = StatusCommand(
            self.kernel
        )



        manager.register(

            AthenaCommand(

                name="status",

                description=
                "Show ATHENA system status",

                callback=status.execute

            )

        )
