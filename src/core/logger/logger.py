from datetime import datetime
from pathlib import Path

LOG_DIR = Path("runtime/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "athena.log"


class AthenaLogger:

    @staticmethod
    def log(level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{timestamp}] [{level}] {message}"

        print(line)

        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")

    @staticmethod
    def info(msg):
        AthenaLogger.log("INFO", msg)

    @staticmethod
    def warning(msg):
        AthenaLogger.log("WARNING", msg)

    @staticmethod
    def error(msg):
        AthenaLogger.log("ERROR", msg)
