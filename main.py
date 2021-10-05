import sys
import PyQt5
from Arquitectura.Vista.vistaPrincipal import Ui_MainWindow as ventanaPrincipal
from Arquitectura.Controlador.flujoControl import *

class MyApp(PyQt5.QtWidgets.QMainWindow, ventanaPrincipal):
    def __init__(self):
        PyQt5.QtWidgets.QMainWindow.__init__(self)
        ventanaPrincipal.__init__(self)
        self.setupUi(self)
        acciones(self)

def acciones(ventana):
    ventana.botonCargar.clicked.connect(lambda: abrirExplorador())
    ventana.botonAceptar.clicked.connect(lambda: analizarCadena(ventana))

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)  # crea un objeto de aplicación (Argumentos de sys)
    window = MyApp()
    window.show()
    app.exec_()


