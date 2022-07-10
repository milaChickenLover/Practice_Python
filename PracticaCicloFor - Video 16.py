# EJERCICIO 1
# for i in range(1,100,2):
#     print(i, end="")

# EJERCICIO 2
clave = input("Escriba una contraseña: ")
todoOk = 1

if len(clave) < 8:
    print("La contraseña debe tener mínimo 8 caracteres.")
    todoOk = 0
else:
    for i in clave:
        if i == " ":
            print("La contraseña no debe tener espacios en blanco")
            todoOk = 0

if todoOk == 1:
    print("Contraseña OK.")
else:
    print("Contraseña errónea.")

# EJERCICIO 3
# for i in correo:
#     if correo == "@" and correo == ".":
#         print("Dirección de correo correcta.")
#     else:
#         print("Dirección de correo incorrecta.")

# correo = input("Digite un correo electrónico: ")
# contadorArroba = 0
# contadorPunto = 0
#
# for i in range(len(correo)):
#     if correo[i] == "@":
#         contadorArroba += 1
#     if correo[i] == ".":
#         contadorPunto += 1
# if contadorArroba == 1 and contadorPunto >= 1:
#     print("Dirección de correo correcta.")
# else:
#     print("Dirección de correo incorrecta.")
