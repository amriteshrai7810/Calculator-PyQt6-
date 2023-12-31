import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QMainWindow, QStatusBar, QToolBar)


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    # noinspection PyTypeChecker
    def _createMenu(self):
        menu = self.menuBar().addMenu('&Menu')
        menu_2 = self.menuBar().addMenu('&Contact')
        menu.addAction("&Exit", self.close)
        menu_2.addAction('&Calculate', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())