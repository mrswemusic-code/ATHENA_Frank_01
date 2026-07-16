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

            return {

                "error":
                f"Command '{name}' not found"

            }



        return command.callback(
            *args,
            **kwargs
        )



    def list_commands(self):


        return list(
            self.commands.keys()
        )



    def help(self):


        result = {}



        for name, command in self.commands.items():

            result[name] = command.description



        return result
