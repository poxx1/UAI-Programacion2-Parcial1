#######################################################################

#PARTE PRACTICA

#######################################################################
#Punto 1
class Personaje:
    vida = 10
    posicion = 0
    velocidad = 24
    def recibir_ataque(self,damage):
        self.vida -= damage
        if self.vida <= 0:
            print("La quedo")
        else:
            print(f"Le quedan {self.vida} puntos de vida al personaje")
    def mover(self,direccion):
        if direccion == "derecha":
            self.posicion += self.velocidad #Muevo el eje X positivamente
            print(f"El personaje se movio a la derecha y ahora se encuentra en la posicion {self.posicion}")
        if direccion == "izquierda":
            self.posicion -= self.velocidad #Muevo el eje Y negativamente
            print(f"El personaje se movio a la izquierda y ahora se encuentra en la posicion {self.posicion}") #{type(self).__name__}
#Punto 2
class Soldado(Personaje):
    ataque = 4
    def atacar(self, victima):
        victima.recibir_ataque(victima,self.ataque)
        #print(f"El personaje ahora tiene {victima.vida} puntos de vida restante") #Spamea banda
#Punto 3
class Campesino(Personaje):
    cosecha = "Maiz"
    cantidadCosechada = 10
    def cosechar(self):
        self.cantidadCosechada += 10
        print(f"El campesino tiene cosechado {self.cantidadCosechada} de {self.cosecha}")

#Punto 5 y Punto 4.
print("########################################################")
print("Programacion II - Lastra Julian - Parcial 1")
print("########################################################")
print("AGE OF EMPIRES 0.1")
print("########################################################")

soldier = Soldado
farmer = Campesino

#Cosechar
print("El campesino esta cosechando.")
farmer.cosechar(farmer)
print("El campesino esta cosechando.")
farmer.cosechar(farmer)

#Mover
print("Muevo al soldado.")
soldier.mover(soldier,"derecha") #Se mueve a la derecha
print("Muevo al soldado.")
soldier.mover(soldier,"izquierda") #Se mueve a la izquierda
print("Muevo al soldado.")
soldier.mover(soldier,"izquierda") #Se mueve a la izquierda
print("Muevo al soldado.")
soldier.mover(soldier,"izquierda") #Se mueve a la izquierda

#Atacar
print("El soldado ataco a un granjero")
soldier.atacar(soldier,farmer) #El soldado ataca al campesino una vez
print("El soldado ataco a un granjero")
soldier.atacar(soldier,farmer) #El soldado ataca al campesino por segunda vez
print("El soldado ataco a un granjero")
soldier.atacar(soldier,farmer) #El soldado mata al campesino

#Punto 4
#El campesino al no tener el metodo atacar, no puede realizar esta accion
try:
    farmer.atacar(farmer,soldier)
except Exception as ex:
    print("El personaje selccionado para realizar el ataque no puede hacerlo.")
#end Punto 4

print("########################################################")
print("#####################    END    ########################")
print("########################################################")
#######################################################################

#PARTE TEORICA

#######################################################################

#Ejercicio 2
a = 1 #En C# para hacer esto tengo que declarar el tipo: int a;
a = "uno" #Como vemos podemos cambiar el tipo de la variable.

#Ejercicio 3
#Python permite las siguientes estructuras condicionales: IF - ELSE - ELIF.
a = 1
if a == 1: #Uso del IF
    print("A = 1")
elif a == 2: #Uso del ELIF - Mas conocido como ELSE IF en otros lenguajes.
    print("A = 2")
else: #Uso del ELSE
    print("La condicion es falsa")

#Ejercicio 4
#Python permite las siguientes estructuras repetitivas: WHILE - FOR
from datetime import datetime
from time import sleep
now = datetime.now()
listCantantes = {"Cerati", "Spinetta","Plant","Jagger"}
for cantante in listCantantes:
    print(f"Nombre del cantante: {cantante}")
while True:
    print(f"La hora es: {now.strftime('%H:%M:%S')}")
    sleep(1)
    break # Corto la ejecucion para poder seguir utilizando lo que queda de parcial.

#Ejercicio 5. 
listAutosDeportivos = ["BMW M3","BMW M3","Ford Mustang"] #Lista
dictAutosDeportivos = {} #Diccionario
dictAutosDeportivos["BMW"] = "M3"
dictAutosDeportivos["Ferrari"] = "Testarossa"
dictAutosDeportivos["Ford"] = "Mustang"
tuplaAutos = ("Nissan", "Nissan", "Ford", "BMW") #Tupla

#Ejercio 6
#Para declarar una clase, hay que utilizar la palabra reservada "class"
class Auto:
    marca = "Nissan" # Propiedad 1
    modelo = "Skyline" # Propiedad 2
    año = 1996 # Propiedad 3
    #Para declarar las propiedades simplemente definimos una "variable".

#Ejercicio 9.
#Dado que no requerimos declarar el tipo, simplemente el polimorfismo se declara:
def volar(loQueVuela):
    print(f"Esta volando {loQueVuela}")
class Animal:
    nombre = "Pato"
class Avion:
    modelo = "737"
volar(Animal)
volar(Avion)
print("########################################################")