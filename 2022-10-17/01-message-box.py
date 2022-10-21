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
    #botones = 0
    #if self.si.isChecked() == True:
      #botones = botones | QMessageBox.Yes
    #if self.no.isChecked() == True:
      #botones = botones | QMessageBox.NO
    #mensaje.setStandardButtons(botones)

    #Todos los botones
    #mensaje.setStandardButtons( QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel | QMessageBox.Ok | QMessageBox.Open | QMessageBox.Close | QMessageBox.Save | QMessageBox.SaveAll | QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)

    mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

    resultado = mensaje.exec()
    if resultado == QMessageBox.Yes:
      print('Se eligio el boton yes')
    if resultado == QMessageBox.No:
      print('Se eligio el boton no')
    if resultado == QMessageBox.Cancel:
      print('Se eligio el boton cancel')


app = QApplication([])

win = MiVentana()
win.show()

app.exec()
