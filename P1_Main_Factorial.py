import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P1_Factorial.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_fact.clicked.connect(self.func)

    # Área de los Slots
    def func(self):

        num = self.txt_num.text()
        self.lbl_fact-setText(num + "!=")
        self.lbl_fact.setFont(QtGui.QFont("Lucida Fax", 18, QtGui.QFont.Bold))

        num = int(self.txt_num.text())
        fact = str(factorial(num))
        self.txt_fact.setText(fact)

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())