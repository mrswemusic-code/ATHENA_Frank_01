import platform
import socket
import datetime
import os

from src.core.logger.logger import AthenaLogger



class IdentityManager:



    def __init__(self):


        self.name = "ATHENA"

        self.codename = "GENESIS"

        self.version = "0.4"


        self.created = (
            "2026-07-16"
        )


        self.hostname = (
            socket.gethostname()
        )


        self.platform = (
            platform.platform()
        )


        self.python = (
            platform.python_version()
        )


        self.path = (
            os.getcwd()
        )



        AthenaLogger.info(
            "Identity Manager initialized."
        )





    def info(self):


        return {


            "name":
            self.name,


            "codename":
            self.codename,


            "version":
            self.version,


            "created":
            self.created,


            "hostname":
            self.hostname,


            "platform":
            self.platform,


            "python":
            self.python,


            "path":
            self.path

        }





    def display(self):


        data = self.info()


        print()

        print(
            "========== ATHENA IDENTITY =========="
        )


        for key,value in data.items():


            print(
                f"{key.upper():12}: {value}"
            )


        print(
            "====================================="
        )
