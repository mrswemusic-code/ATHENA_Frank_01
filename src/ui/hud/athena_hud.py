from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPixmap

import psutil
import subprocess
import socket
import sys
import json
import os
import time


# ============================================================
# ATHENA HUD CONFIGURATION
# ============================================================

BASE_PATH = "/opt/athena/system"

LOGO_PATH = (
    "/opt/athena/branding/logos/"
    "ATHENA_logo_icon.png"
)

STYLE_PATH = (
    "/opt/athena/system/src/ui/styles/"
    "athena_hud.qss"
)

POSITION_FILE = (
    "/opt/athena/system/data/"
    "hud_position.json"
)


# ============================================================
# ATHENA HOLOGRAPHIC HUD
# ============================================================


class AthenaHUD(QWidget):


    def __init__(self):

        super().__init__()


        self.drag_position = None


        self.setWindowTitle(
            "ATHENA CORE HUD"
        )


        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )


        self.setAttribute(
            Qt.WA_TranslucentBackground
        )


        self.resize(
            280,
            340
        )


        self.create_interface()


        self.load_style()


        self.load_position()


        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_system
        )

        self.timer.start(
            1000
        )


        self.update_system()



    # ========================================================
    # UI CREATION
    # ========================================================


    def create_interface(self):


        layout = QVBoxLayout()


        layout.setSpacing(6)



        self.logo = QLabel()


        pixmap = QPixmap(
            LOGO_PATH
        )


        if not pixmap.isNull():

            self.logo.setPixmap(
                pixmap.scaled(
                    70,
                    70,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )


        self.logo.setAlignment(
            Qt.AlignCenter
        )



        self.title = QLabel(
"""
ATHENA CORE
GENESIS v0.4
AI OPERATING SYSTEM
dev by: Mr.Swe
"""
        )



        self.stats = QLabel()



        font = QFont(
            "Liberation Mono",
            9
        )


        self.title.setFont(
            font
        )

        self.stats.setFont(
            font
        )



        self.title.setObjectName(
            "title"
        )


        self.stats.setObjectName(
            "stats"
        )



        layout.addWidget(
            self.logo
        )

        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.stats
        )



        self.setLayout(
            layout
        )



    # ========================================================
    # STYLE
    # ========================================================


    def load_style(self):

        try:

            with open(
                STYLE_PATH,
                "r"
            ) as file:

                self.setStyleSheet(
                    file.read()
                )


        except Exception as error:

            print(
                "HUD STYLE ERROR:",
                error
            )



    # ========================================================
    # SYSTEM MONITOR
    # ========================================================


    def update_system(self):


        cpu = psutil.cpu_percent()


        ram = psutil.virtual_memory().percent


        disk = psutil.disk_usage("/").percent



        battery = psutil.sensors_battery()


        if battery:

            battery_text = (
                f"{battery.percent}%"
            )

        else:

            battery_text = "N/A"



        temperature = self.get_temperature()


        fan = self.get_fan()



        uptime_seconds = (
            time.time()
            -
            psutil.boot_time()
        )


        uptime = (
            int(uptime_seconds // 3600)
        )



        text = f"""

SYSTEM

CPU      {cpu} %
RAM      {ram} %
DISK     {disk} %

TEMP     {temperature}
FAN      {fan}

BAT      {battery_text}
UP       {uptime}h


----------------

CORE

MEMORY   ONLINE
VOICE    READY
AGENTS   READY

ATHENA ACTIVE
"""


        self.stats.setText(
            text
        )


    # ========================================================
    # HARDWARE READERS
    # ========================================================


    def get_temperature(self):

        try:

            result = subprocess.check_output(
                [
                    "sensors"
                ],
                stderr=subprocess.DEVNULL
            ).decode()


            if "Package id 0:" in result:

                line = result.split(
                    "Package id 0:"
                )[1]


                return (
                    line.split()[1]
                )


        except:

            pass


        return "N/A"



    def get_fan(self):

        try:

            result = subprocess.check_output(
                [
                    "sensors"
                ],
                stderr=subprocess.DEVNULL
            ).decode()


            for line in result.splitlines():

                if "RPM" in line:

                    return (
                        line.strip()
                    )


        except:

            pass


        return "N/A"



    # ========================================================
    # MOVEMENT
    # ========================================================


    def mousePressEvent(self,event):

        if event.button() == Qt.LeftButton:

            self.drag_position = (
                event.globalPosition()
                .toPoint()
            )



    def mouseMoveEvent(self,event):

        if self.drag_position:


            delta = (
                event.globalPosition()
                .toPoint()
                -
                self.drag_position
            )


            self.move(
                self.pos()
                +
                delta
            )


            self.drag_position = (
                event.globalPosition()
                .toPoint()
            )



    # ========================================================
    # SAVE POSITION
    # ========================================================


    def closeEvent(self,event):


        data = {

            "x": self.x(),

            "y": self.y()

        }



        try:

            os.makedirs(
                os.path.dirname(
                    POSITION_FILE
                ),
                exist_ok=True
            )


            with open(
                POSITION_FILE,
                "w"
            ) as file:


                json.dump(
                    data,
                    file,
                    indent=4
                )


        except Exception as error:

            print(
                "POSITION SAVE ERROR:",
                error
            )


        event.accept()



    # ========================================================
    # ESC CLOSE
    # ========================================================


    def keyPressEvent(self,event):


        if event.key() == Qt.Key_Escape:

            self.close()



    # ========================================================
    # LOAD POSITION
    # ========================================================


    def load_position(self):


        try:

            with open(
                POSITION_FILE,
                "r"
            ) as file:


                data = json.load(
                    file
                )


                self.move(
                    data["x"],
                    data["y"]
                )


        except:


            self.move(
                60,
                60
            )



# ============================================================
# START
# ============================================================


if __name__ == "__main__":


    app = QApplication(
        sys.argv
    )


    hud = AthenaHUD()


    hud.show()


    sys.exit(
        app.exec()
    )
