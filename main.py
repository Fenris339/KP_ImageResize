from PyQt6 import QtWidgets
from UserInterface import CMainWindow, CApp
import sys

def main():
    app = CApp(sys.argv)
    QtWidgets.QApplication = app
    mainWindow = CMainWindow()
    mainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()