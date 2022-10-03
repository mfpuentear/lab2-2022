from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def  __init__(self):
        super().__init__()
        uic.loadUi("2022-10-03/00-radio.ui", self)

        self.opcion1.toggled.connect(self.on_opcion)
        self.opcion2.toggled.connect(self.on_opcion)
        self.opcion3.toggled.connect(self.on_opcion)

    def on_opcion(self):
        if self.opcion1.isChecked() == True:
            self.etiqueta.setText('opcion 1')
        if self.opcion2.isChecked() == True:
            self.etiqueta.setText('opcion 2')
        if self.opcion3.isChecked() == True:
            self.etiqueta.setText('opcion 3')


app = QApplication([])

win = MiVentana()
win.show()

app.exec()
