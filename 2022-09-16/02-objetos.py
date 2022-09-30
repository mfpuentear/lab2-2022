# Crear objeto Persona:
#   Propiedades: nombre, apellido, edad
#   Metodos:
#     nombre_completo: que devuelva apellido y nombre separado por coma
#     es_mayor: que devuelva True si es mayor o igual a 18 años
 
class Persona:
  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad

  def nombre_completo(self):
    return self.apellido + ', ' + self.nombre
  
  def es_mayor(self):
    return self.edad > 18

persona = Persona('pepe', 'sanchez', 19)
print('nombre completo:', persona.nombre_completo())
print('es mayor:', persona.es_mayor())


# Crear objeto Circulo:
#   Propiedad: radio
#   Metodos: diametro, perimetro y superficie
