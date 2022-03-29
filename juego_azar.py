import random

numero_azar = random.randint (1, 10)


while (True):
     
    numero_jugador = int(input("¿cual es tu número?"))
    

    if numero_azar < numero_jugador:
        print ("el numero es más bajo")
        
    elif numero_azar > numero_jugador:
        print ("el numero es más alto")
        
    else:
        print ("ACERTASTE")
        break



