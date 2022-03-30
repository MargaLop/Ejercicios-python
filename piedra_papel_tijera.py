import random

posibilidades =[1,2,3]
posibles_jugadas = ['Piedra', 'Papel','Tijera']

def num_jugador():

    return int(input('''ELige un número:
    1 - Piedra
    2 - Papel
    3 - Tijera
    ¿Piedra, papel o tijera?:'''))


def num_programa():
    return random.randint(1,3) 



def comparar_jugadas(): 


    while(True):

        pedir_jugador = num_jugador()
        numero_programa = num_programa()

        representacion_humano(pedir_jugador)
        representacion_programa(numero_programa)
        
        
        if numero_programa == pedir_jugador:
            print('EMPATE')
            
        elif pedir_jugador <= 0 or pedir_jugador >= 4:
            print("ERROR")

        elif numero_programa == 3 and pedir_jugador == 1:
            print("HAS GANADO")


        elif numero_programa == 1 and pedir_jugador == 3:
            print("HAS PERDIDO")


        elif numero_programa > pedir_jugador:
            print("HAS PERDIDO")


        elif numero_programa < pedir_jugador:
            print("HAS GANADO")

        

    
        repeticion = ""
        while not repeticion== 'N' and not repeticion == 'n' and not repeticion== 'S' and not repeticion == 's':
            repeticion = input('¿Quieres continuar? S/N')
        if (repeticion== 'N' or repeticion == 'n' ):
            break



def representacion_humano(pedir_jugador):
    

    if pedir_jugador == 1:
        print('''Has elegido PIEDRA:
            _______
        ---'   ____)
             (_____)
             (_____)
              (____)
         ---.__(___)
        ''')

    elif pedir_jugador == 2:
        print('''Has elegido PAPEL:
     
            _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        ''')

    elif pedir_jugador == 3:
        print('''Has elegido TIJERA:
     
            _______
        ---'   ____)____
                  ______)
              __________)
             (____)
        ---.__(___)
        ''')


def representacion_programa(numero_programa):
    
    if numero_programa == 1:
        print('''He elegido PIEDRA:
            _______
        ---'   ____)
             (_____)
             (_____)
              (____)
         ---.__(___)
        ''')

    elif numero_programa == 2:
        print('''He elegido PAPEL:
     
            _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        ''')

    elif numero_programa == 3:
        print('''He elegido TIJERA:
     
            _______
        ---'   ____)____
                  ______)
              __________)
             (____)
        ---.__(___)
        ''')



comparar_jugadas()