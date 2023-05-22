# Verificar si un año es bisiesto.
year = int(input("Ingrese un año: "))
condicion1 = True
condicion2 = False
condicion3 = True

if (year % 4 == 0):
    condicion1 = True
    if (year % 100 == 0):
        condicion2 = False
        if (year % 400 == 0):
            condicion3 = True
        else:
            condicion3 = False
    else:
        condicion2 = True
else:
    condicion1 = False
            
if(condicion1 and condicion2 and condicion3):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")

# DAY 4
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

#Búsqueda del tesoro
row1 = ["¶","¶","¶"]
row2 = ["¶","¶","¶"]
row3 = ["¶","¶","¶"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")
horizontal = position[0]
vertical = position[1]

map[horizontal]


# JUEGO PIEDRA, PAPEL O TIJERAS:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
eleccion = int(input("Escriba su elección: "))
if eleccion >= 3 or eleccion < 0:
    print("Debes elegir un número correcto.")
else:
    print(game_images[eleccion])

    eleccionCompu = random.randint(0, 2)
    print(f"Elección de la computadora: {eleccionCompu}")
    print(game_images[eleccionCompu])

    if eleccion == eleccionCompu:
        print("Empate.")
    elif eleccion == 0 and eleccionCompu == 2:
        print("Tú ganas.")
    elif eleccion == 1 and eleccionCompu == 0:
        print("Tú ganas.")
    elif eleccion == 2 and eleccionCompu == 1:
        print("Tú ganas.")
    else:
        print("Tú pierdes.")
