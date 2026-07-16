import yaml


class UIConfig:


    def __init__(self):

        with open(
            "configs/ui.yaml",
            "r"
        ) as file:

            self.data = yaml.safe_load(file)



    def get(self):

        return self.data["ATHENA_UI"]
