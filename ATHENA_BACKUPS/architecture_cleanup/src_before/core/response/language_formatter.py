class LanguageFormatter:


    def __init__(self):

        self.default_language = "es"


    def format_system_status(
        self,
        data,
        language="es"
    ):


        if language == "es":

            return (

                "Estado del sistema actualizado.\n\n"

                f"CPU: {data.get('cpu')}%\n"

                f"Memoria RAM: {data.get('ram')}%\n"

                f"Disco utilizado: {data.get('disk')}%\n"

                f"Temperatura: {data.get('temperature')}°C"

            )


        return (

            "System status updated.\n\n"

            f"CPU: {data.get('cpu')}%\n"

            f"RAM: {data.get('ram')}%\n"

            f"Disk: {data.get('disk')}%\n"

            f"Temperature: {data.get('temperature')}°C"

        )
