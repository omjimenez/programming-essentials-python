# Factorial de un numero entero

from functools import reduce
def lista_numeros_enteros(numero_factorial):
    lista_numeros_enteros = [ numeros for numeros in range(1, numero_factorial + 1) ]
    return lista_numeros_enteros

def factorial_numero(lista_numeros_enteros):
    resultado_factorial_numero = [reduce(lambda numero1, numero2: numero1 * numero2, lista_numeros_enteros)]
    return resultado_factorial_numero

if __name__ == '__main__':

    factorial = lista_numeros_enteros(4)
    factorial_numero1 = factorial_numero(factorial)
    print(factorial_numero1)
