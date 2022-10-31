import csv

# Abrir archivo
archivo = open('2022-10-31/00-datos.csv')
lector_csv = csv.reader(archivo, delimiter=',', quotechar='"')

# Leer filas
for fila in lector_csv:
  print(fila[0], fila[1], fila[2])

# cerrar archivo
archivo.close()