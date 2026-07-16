import yaml
from pathlib import Path


class ConfigManager:

    def __init__(self):

        self.config_path = Path("configs")

    def load_yaml(self, filename):

        file = self.config_path / filename

        if not file.exists():
            return {}

        with open(file, "r") as f:
            return yaml.safe_load(f)
