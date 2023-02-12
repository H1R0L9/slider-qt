from PySide6 import QtCore, QtWidgets, QtGui
from game import Board
import pickle
import os
import sys

if getattr(sys, "frozen", False):
    absolute_path = os.path.dirname(sys.executable)
elif __file__:
    absolute_path = os.path.dirname(__file__)
relative_path = "assets"

full_path = os.path.join(absolute_path, relative_path)

print(full_path)

class GameWindow(QtWidgets.QWidget):
    def __init__(self, timer):
        super().__init__()
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

        self.timer = timer
        self.board = Board(self.timer)

        self.scrambled = False
        self.solved_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

        self.database_path = os.path.join(full_path, "besttime")
        self.png_path = os.path.join(os.path.join(os.path.dirname(__file__), "assets"), "0.png")

        self.init_game_board(self.board.return_board())

        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def init_game_board(self, board):
        styles = {
            1: "QPushButton { background-color: #FF6767; font-size: 20pt; color: black; }",
            2: "QPushButton { background-color: #FF6767; font-size: 20pt; color: black; }",
            3: "QPushButton { background-color: #FF6767; font-size: 20pt; color: black; }",
            4: "QPushButton { background-color: #FF6767; font-size: 20pt; color: black; }",
            5: "QPushButton { background-color: #FFF153; font-size: 20pt; color: black; }",
            6: "QPushButton { background-color: #78FF5D; font-size: 20pt; color: black; }",
            7: "QPushButton { background-color: #78FF5D; font-size: 20pt; color: black; }",
            8: "QPushButton { background-color: #78FF5D; font-size: 20pt; color: black; }",
            9: "QPushButton { background-color: #FFF153; font-size: 20pt; color: black; }",
            10: "QPushButton { background-color: #73FFDC; font-size: 20pt; color: black; }",
            11: "QPushButton { background-color: #87AFFF; font-size: 20pt; color: black; }",
            12: "QPushButton { background-color: #87AFFF; font-size: 20pt; color: black; }",
            13: "QPushButton { background-color: #FFF153; font-size: 20pt; color: black; }",
            14: "QPushButton { background-color: #73FFDC; font-size: 20pt; color: black; }",
            15: "QPushButton { background-color: #D08FFF; font-size: 20pt; color: black; }"
        }

        self.positions = self.board.return_pos_list()
        self.values = board

        for pos, value in zip(self.positions, self.values):
            button = QtWidgets.QPushButton()
            if value != 0:
                button.setText(str(value))
                button.setStyleSheet(styles.get(value, ""))
            else:
                icon = QtGui.QIcon(QtGui.QPixmap(self.png_path))
                button.setIcon(icon)
                button.setIconSize(button.size())

            button.setFixedSize(50, 50)

            button.setEnabled(False)
            self.grid.addWidget(button, *pos)

    def clear_grid(self):
       for i in range(4):
            for j in range(4):
                item = self.grid.itemAtPosition(i, j).widget()
                self.grid.removeWidget(item)

    def reset_puzzle(self):
        self.setFocus()
        self.board.reset_board()
        self.clear_grid()
        self.init_game_board(self.board.return_board())
        self.update()
        QtWidgets.QApplication.processEvents()
        self.scrambled = False

    def scramble_board(self):
        self.setFocus()
        self.board.scramble_board()
        self.clear_grid()
        self.init_game_board(self.board.return_board())
        self.update()
        QtWidgets.QApplication.processEvents()
        self.scrambled = True

    def output_game_board(self, board):
        print(board)

    def keyPressEvent(self, event):
        if not self.timer.check_is_active() and self.scrambled:
            self.timer.reset_timer()
            self.timer.start_timer()
        else:
            pass

        if event.key() == QtCore.Qt.Key_Up:
            previ, blanki = self.board.move("Up")
        elif event.key() == QtCore.Qt.Key_Down:
            previ, blanki = self.board.move("Down")
        elif event.key() == QtCore.Qt.Key_Left:
            previ, blanki = self.board.move("Left")
        elif event.key() == QtCore.Qt.Key_Right:
            previ, blanki = self.board.move("Right")

        self.do_move(previ, blanki)

        super().keyPressEvent(event)

    def do_move(self, previ, blanki):

        blank = self.grid.itemAtPosition(blanki[0], blanki[1]).widget()
        prev = self.grid.itemAtPosition(previ[0], previ[1]).widget()

        self.grid.removeWidget(blank)
        self.grid.removeWidget(prev)

        self.grid.addWidget(prev, blanki[0], blanki[1])
        self.grid.addWidget(blank, previ[0], previ[1])

        self.check_sovled()

        self.update()

    def check_sovled(self):
        if self.board.return_board() == self.solved_board and self.scrambled:
            self.board.solved()
            self.scrambled = False

    def reset_best_time(self):
        database = open(self.database_path, "ab")
        open(self.database_path, "w").close()
        pickle.dump(1000000, database)
        database.close()