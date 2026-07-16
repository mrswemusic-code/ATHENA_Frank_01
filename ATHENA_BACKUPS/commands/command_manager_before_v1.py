from src.core.logger.logger import AthenaLogger



class CommandManager:


    def __init__(self):

        self.commands = {}



    def register(
        self,
        command
    ):


        self.commands[
            command.name
        ] = command



        AthenaLogger.info(
            f"[COMMAND] Registered {command.name}"
        )




    def execute(
        self,
        name,
        *args,
        **kwargs
    ):


        command = self.commands.get(
            name
        )


        if not command:


            AthenaLogger.info(
                f"[COMMAND] Unknown command {name}"
            )


            return None



        return command.callback(
            *args,
            **kwargs
        )




    def list(self):


        return list(
            self.commands.keys()
        )
