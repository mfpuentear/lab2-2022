from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
  def  __init__(self):
    super().__init__()
    uic.loadUi("2022-10-21/00-combo-box.ui", self)

    self.opciones.currentIndexChanged.connect(self.on_cambio)
    self.agregar.clicked.connect(self.on_agregar)
    self.editar.clicked.connect(self.on_editar)
    self.quitar.clicked.connect(self.on_quitar)

  def on_cambio(self):
    indice = self.opciones.currentIndex()
    opcion = self.opciones.itemText(indice)
    #opcion = self.opciones.currentText()

    self.seleccion.setText(str(indice) + " - " + opcion)
  
  def on_agregar(self):
    self.opciones.addItem("Nuevo item")

  def on_editar(self):
    self.opciones.setItemText(2, "Colorado")

  def on_quitar(self):
    self.opciones.removeItem(2)
    #self.opciones.clear()






app = QApplication([])

win = MiVentana()
win.show()

app.exec()
