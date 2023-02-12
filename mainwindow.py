from PySide6 import QtCore, QtWidgets, QtGui
from gamewindow import GameWindow
from timer import Stopwatch
import qdarktheme
import pickle
import os
import sys

if getattr(sys, "frozen", False):
    absolute_path = os.path.dirname(sys.executable)
elif __file__:
    absolute_path = os.path.dirname(__file__)
relative_path = "assets"
full_path = os.path.join(absolute_path, relative_path)

qdarktheme.enable_hi_dpi()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sliding Puzzle")
        qdarktheme.setup_theme()
        self.database_path = os.path.join(full_path, "besttime")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        self.grid = QtWidgets.QGridLayout()
        central_widget.setLayout(self.grid)

        self.timer = Stopwatch()
        self.game = GameWindow(self.timer)

        self.init_game_ui()

        self.init_interface_ui()

        self.update_best_time()

        self.update_timer = QtCore.QTimer(self)
        self.update_timer.timeout.connect(self.update_best_time)
        self.update_timer.start(1000)


    def init_game_ui(self):
        game_box = QtWidgets.QGroupBox()
        game_box.setStyleSheet("QGroupBox { border: 2px solid gray; border-radius: 5px; }")
        self.grid.addWidget(game_box, 0, 0)

        game_grid = QtWidgets.QGridLayout()
        game_box.setLayout(game_grid)

        game_grid.addWidget(self.game, 0, 0)

    def init_interface_ui(self):
        interface_box = QtWidgets.QGroupBox()
        interface_box.setStyleSheet("QGroupBox { border: 2px solid gray; border-radius: 5px; }")
        self.grid.addWidget(interface_box, 0, 1)

        interface_grid = QtWidgets.QGridLayout()
        interface_box.setLayout(interface_grid)

        interface_grid.addWidget(self.timer, 0, 0)

        self.best_time = QtWidgets.QLabel("Best Time: ")
        interface_grid.addWidget(self.best_time, 1, 0)

        self.scramble_button = QtWidgets.QPushButton("Scramble")
        self.scramble_button.clicked.connect(self.game.scramble_board)
        interface_grid.addWidget(self.scramble_button, 2, 0)

        self.reset_button = QtWidgets.QPushButton("Reset")
        self.reset_button.clicked.connect(self.game.reset_puzzle)
        self.reset_button.clicked.connect(self.timer.reset_timer)
        interface_grid.addWidget(self.reset_button, 3, 0)

        self.reset_time_button = QtWidgets.QPushButton("Reset Best Time")
        self.reset_time_button.clicked.connect(self.game.reset_best_time)
        interface_grid.addWidget(self.reset_time_button, 4, 0)

    def update_best_time(self):
        with open(self.database_path, 'rb') as f:
            data = pickle.load(f)
            f.close()
        self.best_time.setText(f"Best Time: {str(data)}")
