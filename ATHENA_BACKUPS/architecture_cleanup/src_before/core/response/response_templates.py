class ResponseTemplates:


    def __init__(self):

        self.templates = {


            "system":

            "Estado del sistema:\n\n{content}",



            "error":

            "Se produjo un problema:\n\n{content}",



            "information":

            "Información encontrada:\n\n{content}"

        }



    def render(
        self,
        template,
        content
    ):


        selected = self.templates.get(

            template,

            "{content}"

        )


        return selected.format(

            content=content

        )
