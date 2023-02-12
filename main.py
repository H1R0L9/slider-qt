from game import Board
from mainwindow import MainWindow

import sys
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()