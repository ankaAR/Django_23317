'''
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.

En este ejemplo se realizará de forma iterativa.
'''

def get_int():
    while True:
        entero = input('Ingrese un número entero: ')
        try:
            value = int(entero)
        except ValueError:
            print('No es un número entero. Ingrese uno nuevamente.')
        else:
            return value
        
get_int()
