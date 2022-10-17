from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

class MiVentana(QMainWindow):
  def  __init__(self):
    super().__init__()
    uic.loadUi("2022-10-17/01-message-box.ui", self)

    self.mostrar.clicked.connect(self.on_mostrar)

  def on_mostrar(self):
    mensaje = QMessageBox()
    mensaje.setWindowTitle('Titulo de dialogo')
    mensaje.setText('Mensaje a mostrar')

    #Iconos
    #mensaje.setIcon(QMessageBox.Information)
    #mensaje.setIcon(QMessageBox.Question)
    #mensaje.setIcon(QMessageBox.Warning)
    mensaje.setIcon(QMessageBox.Critical)

    #Botones
    mensaje.setStandardButtons( QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel | QMessageBox.Ok | QMessageBox.Open | QMessageBox.Close | QMessageBox.Save | QMessageBox.SaveAll | QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)

    mensaje.exec()



app = QApplication([])

win = MiVentana()
win.show()

app.exec()
