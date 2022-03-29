#import math   
#import itertools                 
#from tracemalloc import start   


lista_ciudades = ["Newyork", "Madrid", "Berlin"]
#numero_ciudades = len(lista_ciudades)                 
'''
def posibilidadviajes(n):

    return math.factorial(n)
'''
#posibilidad = posibilidadviajes(numero_ciudades)


def permutations(lista, final=[]):
    if len(lista) == 0:
        print(final)
    else:
        for i in range(len(lista)):
            permutations(lista[:i] + lista[i+1:], final + lista[i:i+1])



permutacion = permutations(lista_ciudades)
print(permutacion)