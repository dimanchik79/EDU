from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class Menu(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(Menu, self).__init__(parent)
        uic.loadUi("GUI/menu.ui", self)
