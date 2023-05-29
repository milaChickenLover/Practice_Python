# POO Herencia
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculo):

    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

# Heredando de la Clase Vehiculo
class Moto(Vehiculo):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    # Sobreescritura de métodos
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, 
        "\n", self.hcaballito)

class VElectricos(Vehiculo):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)

# Herencia Múltiple
class BicicletaElectrica(VElectricos, Vehiculo):
    pass

# Cuando hay herencia múltiple siempre se da preferencia al Constructor de la primera clase
# que se ha colocado en la herencia, en este caso: VElectricos
miBici = BicicletaElectrica("Montañera", "MV")

# Herencia Super()
class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, ", Edad: ", self.edad, ", Residencia: ", self.lugar_residencia)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

Manuel = Empleado(1500, 55, "Manuel", 55, "Colombia")
Manuel.descripcion()

# El objeto Manuel es de la clase Empleado? -> True
print(isinstance(Manuel, Empleado))
print(isinstance(Manuel, Persona))
<<<<<<< HEAD

#prueba
=======
print(isinstance(Manuel, Persona))

# STRINGS
#nombreUsuario=input("Introduce tu nombre de usuario: ")
#print("El nombre es: ", nombreUsuario.capitalize())

#edad=input("Introduce tu edad: ")

#while(edad.isdigit()==False):
#    print("Por favor, introduce una valor numérico")
#    edad=input("Introduce la edad: ")

#if(int(edad)<18):
#    print("No puedes pasar")
#else:
#    print("Puedes pasar")

#print(edad.isdigit())


# EJERCICIO VIDEO 33
email = input("Introduce un correo electrónico: ")
arroba = email.count("@")

if(arroba!=1 or email.find("@")==0 or email.endswith("@") or email.startswith("@")):
    print("Correo erróneo")
else:
    print("Correo válido")
>>>>>>> 3016c41b03fc48a56f4e89e386647c383f087cb8
