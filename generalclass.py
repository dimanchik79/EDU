import hashlib
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from DB.models import Users


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        uic.loadUi("GUI/main.ui", self)

        self.autorize = [self.txt_username, self.btn_enter, self.txt_password, self.lbl_auth]

        self.menubar.setEnabled(False)

        self.btn_enter.clicked.connect(self.enter_to_program)

    def enter_to_program(self):
        if self.txt_username.text() == "" or self.txt_password.text() == "":
            return

        password = str(hash_password(self.txt_password.text()))
        user = Users.select().where((Users.username == self.txt_username.text()) & (Users.password == password))
        if len(user) == 0:
            return

        for obj in self.autorize:
            obj.hide()

        self.menubar.setEnabled(True)
        self.txt_edu_name.setText(user[0].edu_name+' ')
