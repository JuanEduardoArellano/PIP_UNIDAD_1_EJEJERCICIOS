import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P2_PuntoMedio.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calc.clicked.connect(self.puntoMedio)

    # Área de los Slots
    def puntoMedio(self):

        ax = int(self.txt_ax.text())
        ay = int(self.txt_ay.text())
        bx = int(self.txt_bx.text())
        by = int(self.txt_by.text())

        mx = str((ax + bx) / 2)
        my = str((ay + by) / 2)

        self.txt_medio.setText(mx + "," + my)

    def mensaje(selfself,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())