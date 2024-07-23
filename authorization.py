from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from menu import Menu


class Authorize(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(Authorize, self).__init__(parent)
        uic.loadUi("GUI/authorize.ui", self)

        self.btn_enter.clicked.connect(self.enter_to_program)

    def enter_to_program(self):
        self.hide()

