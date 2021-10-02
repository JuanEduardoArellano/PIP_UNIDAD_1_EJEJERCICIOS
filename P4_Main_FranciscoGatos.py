import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P4_FranciscoGatos.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_conv.clicked.connect(self.conversion)

    # Área de los Slots
    def conversion(self):

        pesos = int(self.txt_pesos.text())
        gatos = 0

        if pesos < 5:
            gatos = 1
        else:
            gatos = pesos / 5

        self.txt_michis.setText(str(gatos))

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())