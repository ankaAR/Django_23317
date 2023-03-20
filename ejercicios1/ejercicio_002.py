'''
Escribir una función que calcule el mínimo común múltiplo entre dos numeros.
'''

def euclides_mcd(a, b):
	if(b == 0):
		return a
	else:
		return euclides_mcd(b, a % b)

def calcular_mcm(a, b):
    mcd = euclides_mcd(a, b)
    mcm = (a * b) // mcd
    return mcm

a = int(input("Ingrese el primer número:"))
b = int(input("Ingrese el segundo número:"))

print("El Minimo común múltiplo es: ", end="")
print(calcular_mcm(a,b))
