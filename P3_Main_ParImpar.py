import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P3_ParImpar.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_res.clicked.connect(self.parImpar)

    # Área de los Slots
    def parImpar(self):

        num = int(self.txt_input.text())

        if num % 2 == 0:
            self.txt_output.setText("PAR")
        else:
            self.txt_output.setText("IMPAR")

    def mensaje(selfself,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())