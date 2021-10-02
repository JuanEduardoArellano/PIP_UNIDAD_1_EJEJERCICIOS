import sys

from math import ceil
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P5_PromedioNnumeros.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    #ATRIBUTO TIPO LISTA PARA ALMACENAR LOS VALORES A PROMEDIAR
    list = []

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_input.clicked.connect(self.ingresar)
        self.btn_prom.clicked.connect(self.promedio)
        self.btn_nuevo.clicked.connect(self.nuevo)
    # Área de los Slots

    def ingresar(self):

        self.list.append(int(self.txt_input.text()))
        self.txt_input.setText("")

    def promedio(self):

        prom = sum(self.list) / len(self.list)

        self.txt_output.setText(str(prom))

    #ELIMINA EL CONTENIDO DE LA LISTA Y BORRA EL ULTIMO RESULTADO
    def nuevo(self):

        self.list = []
        self.txt_output.setText("")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())