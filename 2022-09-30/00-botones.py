from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def  __init__(self):
        super().__init__()
        uic.loadUi("2022-09-30/00-botones.ui", self)

        self.boton_izquierda.setEnabled(False)

        self.boton_izquierda.clicked.connect(self.on_izquierda_clicked)
        self.boton_derecha.clicked.connect(self.on_derecha_clicked)
    
    def on_izquierda_clicked(self):
        self.boton_izquierda.setEnabled(False)
        self.boton_derecha.setEnabled(True)

    def on_derecha_clicked(self):
        self.boton_derecha.setEnabled(False)
        self.boton_izquierda.setEnabled(True)

app = QApplication([])

win = MiVentana()
win.show()

app.exec()
