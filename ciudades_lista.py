#import math   
#import itertools                 
#from tracemalloc import start   

#numero_ciudades = len(lista_ciudades)                 
'''
def posibilidadviajes(n):

    return math.factorial(n)
'''
#posibilidad = posibilidadviajes(numero_ciudades)

lista_ciudades = ["madrid", "Paris"]


def permutations(lista, final=[]):   #sin final no saca nada
    if len(lista) == 0:
        print(final)
       

    else:
        for i in range(len(lista)):                           
            permutations(lista[:i] + lista[i+1:], final + lista[i:i+1])
        

print(permutations(lista_ciudades))