from src.core.logger.logger import AthenaLogger



class AthenaShell:



    def __init__(
        self,
        kernel
    ):

        self.kernel = kernel

        self.bus = kernel.get(
            "command_bus"
        )


        self.running = False





    def start(self):


        AthenaLogger.info(
            "ATHENA Shell ONLINE"
        )


        self.running = True



        print()

        print("=" * 50)

        print(
            "          ATHENA CORE TERMINAL"
        )

        print("=" * 50)

        print()

        print(
            "Type 'help' for commands"
        )

        print()



        while self.running:


            try:


                command = input(
                    "ATHENA > "
                )


                self.process(
                    command
                )



            except KeyboardInterrupt:


                self.stop()





    def process(
        self,
        command
    ):


        command = command.strip()



        if not command:

            return



        if command == "exit":

            self.stop()

            return



        if command == "help":

            self.show_help()

            return



        result = self.bus.dispatch(
            command
        )



        print()


        print(
            result
        )


        print()





    def show_help(self):


        commands = self.kernel.get(
            "commands"
        )


        print()


        print(
            "AVAILABLE COMMANDS:"
        )


        for command in commands.help():

            print(
                "-",
                command
            )


        print()





    def stop(self):


        self.running = False


        AthenaLogger.info(
            "ATHENA Shell OFFLINE"
        )
