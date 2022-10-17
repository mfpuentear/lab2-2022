from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
    def  __init__(self):
        super().__init__()
        uic.loadUi("2022-10-14/01-temperatura.ui", self)

        self.calcular.clicked.connect(self.on_calcular)

    def on_calcular(self):
        temperatura = float(self.temperatura.text())

        resultado = temperatura + 273.15
        
        # Centrigrados a Fahrenheit (T*9/5)+32
        # Fahrenheit a Centrigrados (T-32)*5/9

        self.resultado.setText("{:.3f}".format(resultado))

app = QApplication([])

win = MiVentana()
win.show()

app.exec()
