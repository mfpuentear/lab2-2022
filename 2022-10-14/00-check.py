from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def  __init__(self):
        super().__init__()
        uic.loadUi("2022-10-14/00-check.ui", self)

        self.opcion1.stateChanged.connect(self.on_opcion)
        self.opcion2.stateChanged.connect(self.on_opcion)
        self.opcion3.stateChanged.connect(self.on_opcion)

    def on_opcion(self):
        seleccion = ''
        if self.opcion1.isChecked() == True:
            seleccion = seleccion + 'opcion 1 '
        if self.opcion2.isChecked() == True:
            seleccion = seleccion + 'opcion 2 '
        if self.opcion3.isChecked() == True:
            seleccion = seleccion + 'opcion 3 '
        self.seleccion.setText(seleccion)

app = QApplication([])

win = MiVentana()
win.show()

app.exec()
