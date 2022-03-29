 #ejercicio DAVID
'''
def fibonacci(num):
    suma = 0
    primero = 0
    segundo = 1
    while (suma <= num):
        print(suma)
        primero = segundo
        segundo = suma
        suma = primero+segundo

print(fibonacci(48))
'''
#CON WHILE #FALLO: imprime un numero de más

'''
numero_final_deseado = 15 #int(input("Â¿hasta que numero deseas?:")) 
arr = [1,1]
primer_num = arr[-1]
segundo_num = arr[-2]
longitud_arr = len(arr)
ultimo_numero_arr = arr[longitud_arr-1]



while ultimo_numero_arr <= numero_final_deseado:
    x =(primer_num) + (segundo_num)
    arr.append(x)
    primer_num = arr[-1]
    segundo_num = arr[-2]
    longitud_arr = len(arr) #si esta variable esta fuera del bucle sobre carga el sistema
    ultimo_numero_arr = arr[longitud_arr-1]

arr.pop(-1) #elimina numero de más
print(arr)  '''

#FALLO #ejercicio con for # EL range hace que se imprima tantas veces como indicas 

'''
for x in range(numero_final_deseado):

        x =(primer_num) + (segundo_num)
        arr.append(x)
        primer_num = arr[-1]
        segundo_num = arr[-2]

print(arr)
'''

#ejecicio con while # copia david
'''
numero_final_deseado = int(input("¿hasta que numero deseas?:")) 
arr = []
primer_numero = 0
segundo_num = 1
ultimo_numero_arr = 0
suma = 1


while suma <= numero_final_deseado:
    arr.append(suma)
    suma = (primer_numero) + (segundo_num)
    primer_numero  = segundo_num
    segundo_num = suma'''


#ejercicio definitivo con while

'''
numero_final_deseado = int(input("¿hasta que numero deseas?:")) 
arr = [0,1]
suma = 1


while suma <= numero_final_deseado:
    arr.append(suma)
    suma = arr [-1] + arr[-2]
    

print(arr)
'''


def fibonacci(i):

    if i <= 1:
        return i
    else:
        return fibonacci(i-1) + fibonacci(i-2)
    
    lista_vacia =[]
    contadpr = -1

    while fibonacci(contador) < 50:
        contador += 1
        lista_vacia.append(contador)
        
        print(lista_vacia)

fibonacci(90)
