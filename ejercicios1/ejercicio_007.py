'''
Crear una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
- mostrar(): Muestra los datos de la cuenta.
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
'''

class Cuenta():

    def __init__(self,titular,cantidad=0.0):
        self.titular=titular
        self.__cantidad=cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

       
    def mostrar(self):
        return "Cuenta\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

#Ejemplo de implementación y uso

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar(self):
        return self.nombre + " " + self.apellido


persona1 = Persona("James", "Bond")
cuenta1 = Cuenta(persona1, 1000.0)
print(cuenta1.mostrar())
cuenta1.ingresar(500.0)
print(cuenta1.mostrar())
cuenta1.retirar(200.0)
print(cuenta1.mostrar())