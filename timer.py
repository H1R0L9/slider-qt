import sys
from PySide6 import QtWidgets, QtCore

class Stopwatch(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.lcd = QtWidgets.QLCDNumber(self)
        self.lcd.setMinimumHeight(48)
        self.lcd.setDigitCount(10)
        self.lcd.display("0.0")

        self.grid.addWidget(self.lcd, 0, 0)

        self.time = 0

    def start_timer(self):
        self.timer.start(10)

    def stop_timer(self):
        self.timer.stop() 

    def reset_timer(self):
        self.timer.stop()
        self.time = 0
        self.lcd.display("0.0")

    def update_timer(self):
        self.time += 0.01
        self.lcd.display("{:.3f}".format(self.time))

    def check_is_active(self):
        if self.timer.isActive():
            return True
        else:
            return False

    def return_value(self):
        return self.time