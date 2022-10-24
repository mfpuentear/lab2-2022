from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class MiVentana(QMainWindow):
  def  __init__(self):
    super().__init__()
    uic.loadUi("2022-10-24/00-lista.ui", self)

    #self.lista.itemSelectionChanged.connect(self.on_item_selection_changed)
    #self.lista.itemClicked.connect(self.on_item_clicked)
    self.lista.currentItemChanged.connect(self.on_current_item_changed)

    # Agregar item a la lista
    #self.lista.addItem('Texto')

    # Editar item de la lista
    #item.setText('nuevo texto')

    # Quitar item de la lista
    #self.lista.takeItem(fila)

    # Quitar todos los item de la lista
    #self.lista.clear()

    # Obtener item a partir de fila
    #self.lista.item(fila)

  def on_item_selection_changed(self):
    print("seleccion")
    item = self.lista.currentItem()
    self.seleccion.setText(item.text())
  
  def on_item_clicked(self, item):
    print("seleccion")
    self.seleccion.setText(item.text())

  def on_current_item_changed(self, itemActual, itemAnterior):
    print("Seleccion")
    #self.lista.row(item)
    self.seleccion.setText(str(self.lista.currentRow()) + " - " + itemActual.text())
    if itemAnterior:
      print("Anterior: " + itemAnterior.text() + ", Actual: " + itemActual.text())


app = QApplication([])

win = MiVentana()
win.show()

app.exec()
