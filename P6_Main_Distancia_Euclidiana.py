import sys
from math import sqrt
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P6_Distancia_Euclidiana.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.vectorx = []
        self.vectory = []

        # Área de los Signals
        self.btn_anadir.clicked.connect(self.anadir)
        self.btn_calc.clicked.connect(self.calcular)

    #Area de slots

    def anadir(self):

        if self.txt_x.text() == "":
            self.vectorx.append(0)
        else:
            self.vectorx.append(int(self.txt_x.text()))

        if self.txt_y.text() == "":
            self.vectory.append(0)
        else:
            self.vectory.append(int(self.txt_y.text()))

        self.txt_x.setText("")
        self.txt_y.setText("")

    def calcular(self):

        susx = self.vectorx[0]
        for i in range(1, len(self.vectorx)):
            susx = abs(pow(susx - self.vectorx[i], 2))
        print(susx)
        susy = self.vectory[0]
        for i in range(1, len(self.vectory)):
            susy = abs(pow(susy - self.vectory[i], 2))
        print(susy)

        de = sqrt(susx + susy)

        self.txt_res.setText(str(de))

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())