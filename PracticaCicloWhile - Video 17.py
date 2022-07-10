# PREGUNTA 1
# numeroIngresado = int(input("Escriba un número: "))
# numeroAnterior = numeroIngresado - 1
#
# while numeroIngresado > numeroAnterior:
#     numeroAnterior = numeroIngresado
#     numeroIngresado = int(input("Escriba un número: "))
#     print(numeroIngresado)


# PREGUNTA 2
numeroPositivo = int(input("Escriba un número positivo: "))
acumulando = 0

while numeroPositivo > 0:
    if acumulando == 0:
        acumulando = numeroPositivo

    numeroPositivo = int(input("Escriba otro número positivo: "))
    acumulando += numeroPositivo
    print(f"La suma acumulada de los números ingresados es: {acumulando}")
