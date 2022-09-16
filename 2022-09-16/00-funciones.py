# Realizar una funcion que devuelva el mayor de dos numeros
def mayor(a, b):
  if a>b:
    return a
  return b

# Realizar una funcion que devuelva el menor de dos numeros
def menor(a, b):
  if a<b:
    return a
  return b

# Realizar una funcion que devuelva el mayor de tres numeros
def mayor3(a,b,c):
  return mayor(a, mayor(b,c))

x = 10
y = 4
z = 13

print('El mayor es:', mayor(x,y))
print('El menor es:', menor(x,y))

print('El mayor de tres es:', mayor3(x,y,z))