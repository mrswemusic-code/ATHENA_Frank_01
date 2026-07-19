from src.core.commands.command import AthenaCommand

from src.core.commands.system.status import StatusCommand
from src.core.commands.system.health import HealthCommand
from src.core.commands.system.diagnostics import DiagnosticsCommand
from src.core.commands.system.runtime import RuntimeCommand


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


        commands = [

            AthenaCommand(

                name="status",

                description="Show ATHENA system status",

                callback=StatusCommand(
                    self.kernel
                ).execute

            ),

            AthenaCommand(

                name="health",

                description="Show ATHENA health",

                callback=HealthCommand(
                    self.kernel
                ).execute

            ),

            AthenaCommand(

                name="diagnostics",

                description="Run diagnostics",

                callback=DiagnosticsCommand(
                    self.kernel
                ).execute

            ),

            AthenaCommand(

                name="runtime",

                description="Show runtime information",

                callback=RuntimeCommand(
                    self.kernel
                ).execute

            )

        ]


        for command in commands:

            manager.register(
                command
            )
