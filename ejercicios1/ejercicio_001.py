'''
Escribir una función que calcule el máximo común divisor entre dos números.
'''

def euclides_mcd(a, b):
	if(b == 0):
		return a
	else:
		return euclides_mcd(b, a % b)

a = int(input("Ingrese el primer número:"))
b = int(input("Ingrese el segundo número:"))

print("El Máximo común divisor es: ", end="")
print(euclides_mcd(a,b))

