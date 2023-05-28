<<<<<<< HEAD
from pickle import FALSE
from platform import java_ver
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED


for a in range(0, 5):
    print("Hello World from python on a chromebook")

nombre = input("¿Como te llamas?")
print("Hola " + nombre)

edad = int(input("¿Cual es tu edad?"))
masDe12 = edad >= 12
respuestaHijoDelDueño = input("¿Es Hijo del Dueno?")
esHijoDelDueño = respuestaHijoDelDueño == "Sí"
puedePasar = masDe12 or esHijoDelDueño

if puedePasar:
    print("Usted puede pasar a la montaña rusa")
else:
    print("Usted no puede pasar a la montaña rusa")

# ***********************************************************************************************
x = 8
y = 7
z = 0
result1 = x == y
result2 = y > x
result3 = z < x + 2
print(not (False and True))
# CONDICIONALES
x = input('Name: ')
if x == 'Mila':
 print(x + ' you are awsome!')
elif x == 'Nao':
 print("Hello " + x + ' How are you?')
elif x == 'Kaori':
 print("Hello " + x + ' you are great!')
else:
 print("Hello no one, you are suck!")
# **************************************** COLECCIONES *******************************************
# LISTAS
x = [5, True, "Maic"]
#cantidad de elementos en la lista
print(len(x))
#agrega elementos a la lista
x.append("hello")
#agrega elementos a la lista al final
x.extend([5,6,7,8])
print(x)
#remover el ultimo indice de la lista
print(x.pop(0))
#acceder al valor de un indice de la lista
print(x[1])
#cambiar el valor de un indice de la lista
x[0] = "hello"
print(x)
#copiar una lista
y = x[:]
#Las listas contienen otroos elementos de colecciones como otras listas, tuplas, listas dentro de otras listas
x = [[],(),[[],[],[3,5,6]]]
# TUPLAS / Son inmutables
x = (0,0,2,2,3)
print(x[0])

# start, stop, step
# start by default with 0 and goes up to the number I put in range if I put one number.
# If I put 2 numbers (1, 10) it stops until the previous number that I put in range, step
for i in range(10):
 print(i)
for i in [1,2,3,5]:
 print(i)
x = [1,2,3,5]
# enumerate es igual que colocar for i in range(len(x)): 
#print(x[i])
for i, element in enumerate(x):
    print(i, element)
# While condition
while i < 10:
    print('run')
    i += 1
# ESTO ES UN BUCLE INFINITO
#while True:
# print('run')
# i += 1
# if i == 10:
# break
# SLICE OPERATOR
x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "hello"
#sliced = [start:stop:step]
sliced = x[0:4:-2]
print(sliced)
# si algun espacio se queda en blanco tomara por defecto los siguientes datos:
# sliced = [start:stop:step]
# sliced = [::]
# sliced = [comienza por el principio:para hasta el final:va de 1 en 1]
# COLECCION SET
x = set()
s = {3,2,2} # Diccionario
s2 = [3,32,2,2,2]
s.add(5)
s.remove(2)
print(s)
print(3 in s)
print(s.union(s))
print(s.difference(s))
print(s.intersection(s))
# DICCIONARIOS
x = {'key': 5}
x['key2'] = 5
x[2] = [2,2,1,1]
print(x)
# chequear si existe un elemento en un diccionario
print('key' in x)
# obtener el valor de un diccionario
print(x.values())
# para borrar un elemento del diccionario
del x['key']
print(x)
z = {'key': 6}
for key, value in z.items():
 print(key,value)
# COMPRENHENSIONS (COMPRENSIONES DE LISTAS)
x = [0 for x in range(5)]
print(x)
q = [[0 for q in range(100)] for q in range(5)]
print(q)
r = [i for i in range(100) if i % 5 == 0]
print(r)
r = {i: 0 for i in range(100) if i % 5 == 0}
print(r)
r = {i for i in range(100) if i % 5 == 0}
print(r)
r = tuple(i for i in range(100) if i % 5 == 0)
print(r)

# ************************************** FUNCIONES *********************************************
# Definiendo una funcion
def func():
 print('run')
func()
# anidando funciones
def func():
   print('run')
   def func():
      print('maic')
func()
# funciones con parametros
def func(x,y):
 print('run', x, y)
 return x * y, x / y
print(func(5, 6))
# mas utilidades de las funciones
def func(x,y,z=None):
    print('run', x, y, z)
    return x * y, x / y
r1, r2 = func(5, 6, 7)
print(r1, r2)

# UNPACK OPERATOR / *ARGS AND **KWARGS
def func(*args):
    return print(sum(args)*0.05)
func(3,30,40,56,906)
# los args kwargs sirven para separar elementos de sus colecciones, siempre devuelve una tupla
def func(*args, **kwargs):
 pass
x = [1,23,236363,2727]
print(x)
print(*x)
# otro ejemplo de desempaquetar
def func(x, y):
    print(x, y)
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(*pair)
# otro ejemplo de desempaquetar
def func(x, y):
    print(x, y)
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(**{'x': 2, 'y': 5})
# ejemplo con argumentos y kwargumentos juntos
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('Me gustaria {} {}'.format(args[0],kwargs['comida']))
func(10,20,30,fruta='fresa',comida='leche',animal='perro')

# SCOPE AND GLOBAL / ALCANCE DE LAS VARIABLES
x = 'tim'
def func(name):
    global x #boorando esta linea la x no cambiara de valor
    x = name
print(x)
func('changed')
print(x)

# EXCEPCIONES
#raise Exception('Bad')
#raise FileExistsError('')

# MANEJO DE EXCEPCIONES
try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('finally')

# LAMBDAS : Es esencialmente una funcion anonima de una linea
x = lambda x, y: x + y
print(x(2, 32))
# MAP AND FILTER
x = [1,2,4,5,3,3,21,2,21,2,313,1,23,142,4]
mp = map(lambda i: i + 2, x)
print(list(mp))
#otra forma
mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))
#en vez de usar una fuuncion se usa lambda
def func(i):
    i = i * 3
    return i % 2 == 0
mp = filter(func, x) #aqui se usa mejor lambda
print(list(mp))
# F STRINGS
tim = 89
x = f'hello {6 + 8} {tim} {67 + 9}'
print(f'hello {tim}')

# ***************************** PROGRAMACION ORIENTADA A OBJETOS ********************************

# En una clase siempre se va a definir la funcion INIT para que inicie los parametros

# Class NombreDeClase():
    # def __init__(self,param1,param2):
        # self.param1 = param1
        # self.param2 = param2
    # def otraFuncion(self):
        # accion
        # print(self.param1)

class Perro():
    def __init__(self,raza,nombre,puntos,edad):
        # Atributos
        self.raza = raza
        self.nombre = nombre
        # esperamos valor booleano
        self.puntos = puntos
        self.edad = edad

haskie = Perro(raza='haskie', nombre='Sam', puntos=FALSE, edad=5)

# HERENCIA


# MANEJO DE ARCHIVOS

# Abrir archivo
with open("Frases_famosas.txt","r") as archivo:
    for linea in archivo:
        print("=== Frase ===")
        print(linea)
#Modos de Apertura de Archivos
#r (read - leer)
#w (write - escribir)
#a (append - añadir) añadir información al final del archivo
#Agregar un + incluye leer. Por ejemplo: w+ es escribir y leer.

# Modificar archivo. Dos formas: Reemplazar contenido y Añadir contenido.
notas = {
    "Nora": 87,
    "Gino": 100,
    "Loretto": 67,
    "Dalina": 45
}

with open("data_estudiantes.txt", "w") as archivo:
    for normbre, nota in notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")

nuevas_notas = {
    "Emily": 54,
    "Daniel":98,
    "Julienne":78
}

with open("data_estudiantes.txt",'a') as archivo:
    for nombre, nota in nuevas_notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")


# IMPORTACIONES

#Módulo: Un archivo python que contiene definiciones y sentencias. Se busca que estén relacionados.
#Importación: Sentencia que da acceso a las funciones y constantes definidas en el módulo importado.
#import modulo.funcion(args)
import math
exponente = math.pow(9,2)
print(exponente)

import math as matematicas
matematicas.pi

#otra forma de importar un solo módulo a usar:
from math import pow
pow(9,2)


#ERRORES Y EXCEPCIONES

#Error de Sintaxis: SyntaxError: 
#   Código mal escrito
#Excepción: IndexError, KeyError, NameError, ZeroDivisionError, RecursionError: 
#   Error detectado durante la ejecución de un programa
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

try:
    # Intenta ejecutar este código
    resultado = num1 / num2
    print(f"{num1} / {num2} =", resultado)
except ZeroDivisionError:
    # Si ocurre una expceción, detente inmediatamente y ejecuta este código
    print("Alerta, Excepcion.")





=======
from pickle import FALSE
from platform import java_ver
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED


for a in range(0, 5):
    print("Hello World from python on a chromebook")

nombre = input("¿Como te llamas?")
print("Hola " + nombre)

edad = int(input("¿Cual es tu edad?"))
masDe12 = edad >= 12
respuestaHijoDelDueño = input("¿Es Hijo del Dueno?")
esHijoDelDueño = respuestaHijoDelDueño == "Sí"
puedePasar = masDe12 or esHijoDelDueño

if puedePasar:
    print("Usted puede pasar a la montaña rusa")
else:
    print("Usted no puede pasar a la montaña rusa")

# ***********************************************************************************************
x = 8
y = 7
z = 0
result1 = x == y
result2 = y > x
result3 = z < x + 2
print(not (False and True))
# CONDICIONALES
x = input('Name: ')
if x == 'Mila':
 print(x + ' you are awsome!')
elif x == 'Nao':
 print("Hello " + x + ' How are you?')
elif x == 'Kaori':
 print("Hello " + x + ' you are great!')
else:
 print("Hello no one, you are suck!")
# **************************************** COLECCIONES *******************************************
# LISTAS
x = [5, True, "Maic"]
#cantidad de elementos en la lista
print(len(x))
#agrega elementos a la lista
x.append("hello")
#agrega elementos a la lista al final
x.extend([5,6,7,8])
print(x)
#remover el ultimo indice de la lista
print(x.pop(0))
#acceder al valor de un indice de la lista
print(x[1])
#cambiar el valor de un indice de la lista
x[0] = "hello"
print(x)
#copiar una lista
y = x[:]
#Las listas contienen otroos elementos de colecciones como otras listas, tuplas, listas dentro de otras listas
x = [[],(),[[],[],[3,5,6]]]
# TUPLAS / Son inmutables
x = (0,0,2,2,3)
print(x[0])

# start, stop, step
# start by default with 0 and goes up to the number I put in range if I put one number.
# If I put 2 numbers (1, 10) it stops until the previous number that I put in range, step
for i in range(10):
 print(i)
for i in [1,2,3,5]:
 print(i)
x = [1,2,3,5]
# enumerate es igual que colocar for i in range(len(x)): 
#print(x[i])
for i, element in enumerate(x):
    print(i, element)
# While condition
while i < 10:
    print('run')
    i += 1
# ESTO ES UN BUCLE INFINITO
#while True:
# print('run')
# i += 1
# if i == 10:
# break
# SLICE OPERATOR
x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "hello"
#sliced = [start:stop:step]
sliced = x[0:4:-2]
print(sliced)
# si algun espacio se queda en blanco tomara por defecto los siguientes datos:
# sliced = [start:stop:step]
# sliced = [::]
# sliced = [comienza por el principio:para hasta el final:va de 1 en 1]
# COLECCION SET
x = set()
s = {3,2,2} # Diccionario
s2 = [3,32,2,2,2]
s.add(5)
s.remove(2)
print(s)
print(3 in s)
print(s.union(s))
print(s.difference(s))
print(s.intersection(s))
# DICCIONARIOS
x = {'key': 5}
x['key2'] = 5
x[2] = [2,2,1,1]
print(x)
# chequear si existe un elemento en un diccionario
print('key' in x)
# obtener el valor de un diccionario
print(x.values())
# para borrar un elemento del diccionario
del x['key']
print(x)
z = {'key': 6}
for key, value in z.items():
 print(key,value)
# COMPRENHENSIONS (COMPRENSIONES DE LISTAS)
x = [0 for x in range(5)]
print(x)
q = [[0 for q in range(100)] for q in range(5)]
print(q)
r = [i for i in range(100) if i % 5 == 0]
print(r)
r = {i: 0 for i in range(100) if i % 5 == 0}
print(r)
r = {i for i in range(100) if i % 5 == 0}
print(r)
r = tuple(i for i in range(100) if i % 5 == 0)
print(r)

# ************************************** FUNCIONES *********************************************
# Definiendo una funcion
def func():
 print('run')
func()
# anidando funciones
def func():
   print('run')
   def func():
      print('maic')
func()
# funciones con parametros
def func(x,y):
 print('run', x, y)
 return x * y, x / y
print(func(5, 6))
# mas utilidades de las funciones
def func(x,y,z=None):
    print('run', x, y, z)
    return x * y, x / y
r1, r2 = func(5, 6, 7)
print(r1, r2)

# UNPACK OPERATOR / *ARGS AND **KWARGS
def func(*args):
    return print(sum(args)*0.05)
func(3,30,40,56,906)
# los args kwargs sirven para separar elementos de sus colecciones, siempre devuelve una tupla
def func(*args, **kwargs):
 pass
x = [1,23,236363,2727]
print(x)
print(*x)
# otro ejemplo de desempaquetar
def func(x, y):
    print(x, y)
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(*pair)
# otro ejemplo de desempaquetar
def func(x, y):
    print(x, y)
pairs = [(1,2), (3,4)]
for pair in pairs:
    func(**{'x': 2, 'y': 5})
# ejemplo con argumentos y kwargumentos juntos
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('Me gustaria {} {}'.format(args[0],kwargs['comida']))
func(10,20,30,fruta='fresa',comida='leche',animal='perro')

# SCOPE AND GLOBAL / ALCANCE DE LAS VARIABLES
x = 'tim'
def func(name):
    global x #boorando esta linea la x no cambiara de valor
    x = name
print(x)
func('changed')
print(x)

# EXCEPCIONES
#raise Exception('Bad')
#raise FileExistsError('')

# MANEJO DE EXCEPCIONES
try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('finally')

# LAMBDAS : Es esencialmente una funcion anonima de una linea
x = lambda x, y: x + y
print(x(2, 32))
# MAP AND FILTER
x = [1,2,4,5,3,3,21,2,21,2,313,1,23,142,4]
mp = map(lambda i: i + 2, x)
print(list(mp))
#otra forma
mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))
#en vez de usar una fuuncion se usa lambda
def func(i):
    i = i * 3
    return i % 2 == 0
mp = filter(func, x) #aqui se usa mejor lambda
print(list(mp))
# F STRINGS
tim = 89
x = f'hello {6 + 8} {tim} {67 + 9}'
print(f'hello {tim}')

# ***************************** PROGRAMACION ORIENTADA A OBJETOS ********************************

# En una clase siempre se va a definir la funcion INIT para que inicie los parametros

# Class NombreDeClase():
    # def __init__(self,param1,param2):
        # self.param1 = param1
        # self.param2 = param2
    # def otraFuncion(self):
        # accion
        # print(self.param1)

class Perro():
    def __init__(self,raza,nombre,puntos,edad):
        # Atributos
        self.raza = raza
        self.nombre = nombre
        # esperamos valor booleano
        self.puntos = puntos
        self.edad = edad

haskie = Perro(raza='haskie', nombre='Sam', puntos=FALSE, edad=5)

# HERENCIA


# MANEJO DE ARCHIVOS

# Abrir archivo
with open("Frases_famosas.txt","r") as archivo:
    for linea in archivo:
        print("=== Frase ===")
        print(linea)
#Modos de Apertura de Archivos
#r (read - leer)
#w (write - escribir)
#a (append - añadir) añadir información al final del archivo
#Agregar un + incluye leer. Por ejemplo: w+ es escribir y leer.

# Modificar archivo. Dos formas: Reemplazar contenido y Añadir contenido.
notas = {
    "Nora": 87,
    "Gino": 100,
    "Loretto": 67,
    "Dalina": 45
}

with open("data_estudiantes.txt", "w") as archivo:
    for normbre, nota in notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")

nuevas_notas = {
    "Emily": 54,
    "Daniel":98,
    "Julienne":78
}

with open("data_estudiantes.txt",'a') as archivo:
    for nombre, nota in nuevas_notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")


# IMPORTACIONES

#Módulo: Un archivo python que contiene definiciones y sentencias. Se busca que estén relacionados.
#Importación: Sentencia que da acceso a las funciones y constantes definidas en el módulo importado.
#import modulo.funcion(args)
import math
exponente = math.pow(9,2)
print(exponente)

import math as matematicas
matematicas.pi

#otra forma de importar un solo módulo a usar:
from math import pow
pow(9,2)


#ERRORES Y EXCEPCIONES

#Error de Sintaxis: SyntaxError: 
#   Código mal escrito
#Excepción: IndexError, KeyError, NameError, ZeroDivisionError, RecursionError: 
#   Error detectado durante la ejecución de un programa
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

try:
    # Intenta ejecutar este código
    resultado = num1 / num2
    print(f"{num1} / {num2} =", resultado)
except ZeroDivisionError:
    # Si ocurre una expceción, detente inmediatamente y ejecuta este código
    print("Alerta, Excepcion.")





>>>>>>> 566e6157cc814851110273e4f4e3108d6069e4ba
