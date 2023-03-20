'''
Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
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

def palabra_mas_repetida(diccionario):
    palabra_max = ""
    frecuencia_max = 0
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    return (palabra_max, frecuencia_max)

cadena = input("Ingrese el texto:")
diccionario = contar_palabras(cadena)
print(diccionario)
palabra_max, frecuencia_max = palabra_mas_repetida(diccionario)
print(f"La palabra más repetida es '{palabra_max}' con frecuencia {frecuencia_max}.")
