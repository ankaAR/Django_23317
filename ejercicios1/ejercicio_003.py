'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''

def contar_palabras(cadena):
    diccionario = {}
    palabras = cadena.split()
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

cadena = input("Ingrese el texto:")
resultado = contar_palabras(cadena)
print(resultado)
