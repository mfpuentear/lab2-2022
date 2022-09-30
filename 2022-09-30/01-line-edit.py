from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def  __init__(self):
        super().__init__()
        uic.loadUi("2022-09-30/01-line-edit.ui", self)

        self.mostrar.clicked.connect(self.on_mostrar)
    
    def on_mostrar(self):
        mensaje = self.entradaMensaje.text()
        self.mensaje.setText(mensaje)

app = QApplication([])

win = MiVentana()
win.show()

app.exec()
