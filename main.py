from PyQt6 import QtCore, QtGui, QtWidgets

from windows.login import Ui_loginWindow


if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec())