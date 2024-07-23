import hashlib
import sys

from DB.models import Users

from PyQt5.QtWidgets import QApplication
from authorization import Authorize


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def main():
    password = hash_password("password")
    print(password)

    application = QApplication(sys.argv)
    main_window = Authorize()
    main_window.show()
    sys.exit(application.exec())


if __name__ == "__main__":
    main()
