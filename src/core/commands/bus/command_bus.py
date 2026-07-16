from src.core.logger.logger import AthenaLogger



class CommandBus:


    def __init__(
        self,
        manager
    ):

        self.manager = manager



    def dispatch(
        self,
        command_name,
        *args,
        **kwargs
    ):


        AthenaLogger.info(
            f"[BUS] Dispatch command: {command_name}"
        )


        result = self.manager.execute(

            command_name,

            *args,

            **kwargs

        )


        return result

