from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic

class MiVentana(QMainWindow):
  def  __init__(self):
    super().__init__()
    uic.loadUi("2022-10-28/00-tabla.ui", self)

    # Especificar cuantas columnas hay
    self.tabla.setColumnCount(3)
    
    # Insertar columna
    #self.tabla.insertColumn(nro)

    # Nombrar las columnas
    self.tabla.setHorizontalHeaderLabels(('Nombre', 'Apellido', 'email'))

    # Modicar nombre de columna
    self.tabla.setHorizontalHeaderItem(2, QTableWidgetItem('e-mail'))

    # Cantidad de filas
    filas = self.tabla.rowCount()

    # Agregar fila a la tabla
    self.tabla.insertRow(filas)
    self.tabla.setItem(filas, 0, QTableWidgetItem('Pepe'))
    self.tabla.setItem(filas, 1, QTableWidgetItem('Sanchez'))
    self.tabla.setItem(filas, 2, QTableWidgetItem('psanchez@mail.com'))

    filas = self.tabla.rowCount()
    self.tabla.insertRow(filas)
    self.tabla.setItem(filas, 0, QTableWidgetItem('Juan'))
    self.tabla.setItem(filas, 1, QTableWidgetItem('Perez'))
    self.tabla.setItem(filas, 2, QTableWidgetItem('jperez@mail.com'))

    # Quitar fila
    #self.tabla.removeRow(fila)

    # Quitar columna
    #self.tabla.removeColumn(columna)

    # Señales
    #self.tabla.cellClicked.connect(self.on_cell_clicked)
    self.tabla.itemSelectionChanged.connect(self.on_item_selection_changed)

  
  def on_cell_clicked(self, fila, columna):
    print(fila, columna)
    item = self.tabla.item(fila, columna)
    self.seleccion.setText(item.text())

  def on_item_selection_changed(self):
    item = self.tabla.currentItem()
    if item:
      print(item.text(), item.row(), item.column())



app = QApplication([])

win = MiVentana()
win.show()

app.exec()
