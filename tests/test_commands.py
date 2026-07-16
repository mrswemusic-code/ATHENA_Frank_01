from src.core.commands.command import AthenaCommand
from src.core.commands.command_manager import CommandManager



manager = CommandManager()



def hello():

    print(
        "ATHENA COMMAND ONLINE"
    )



command = AthenaCommand(

    name="hello",

    description="Test command",

    callback=hello

)



manager.register(
    command
)



manager.execute(
    "hello"
)



print(
    manager.list()
)
