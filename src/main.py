import sys
from PySide6 import QtWidgets, QtGui

from src.config import APP_NAME
from utils import resource_path

ICON_FILEPATH = resource_path('icon.ico')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main_window = MainWindow()

    main_window.setWindowTitle(APP_NAME)

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(ICON_FILEPATH),
                   QtGui.QIcon.Normal, QtGui.QIcon.Off)
    main_window.setWindowIcon(icon)

    main_window.show()

    sys.exit(app.exec())
