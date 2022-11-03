import random
import list1
from list1 import words
from itertools import cycle, islice

secret_word = random.choice(words)
secret_word = list(secret_word)
contador = len(secret_word)

 ###### CREACIÓN DE FUNCION ######

 #1.- Función que busca la posición de cada carácter repetido.

def list_duplicates_of(seq,item):
    start_at = -1 # Para matchear correctamente el index
    locs = [] # Para almacenar los index de los valores duplicados
    while True:
        try:
            loc = seq.index(item,start_at+1) 
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs



def hangman():
    
     #1 ------------------------

    secret_word = random.choice(words) #Palabra random en base a nuestra lista.

    secret_word_string_2 = secret_word #Guardamos el valor antes de modificarlo en otra var.

    letters = len(secret_word) #Contador de letras en palabra.

    secret_word_censure = "_"*letters #Convertimos letras en "_" en base a la var letters

    secret_word_censure = list(secret_word_censure) #Convertimos la palabra en lista para poder modificarla.

    secret_word = list(secret_word) #Convertimos en lista para compararlo luego con secret_word_censure.

    secret_word_string = "".join(secret_word_censure) #Volvemos string y sin ningún espacio a secret_word_censure.


    lives = 7

    print("¡Hola!, estás jugando Hangman, a continuación podrás observar la palabra secreta, tus vidas y tu progreso:")
    print(f"¡Comenzamos! La palabra secreta es: {secret_word_string}, y tienes {lives} Vidas")
    
    letters_player = [] #Var para guardar las letras recibidas de input

#INPUT + BUCLE
 
    while lives > 0: #Mientras las vidas sean mayores que 0 (continuar)
        
       

        u_pick = input("Ingresa una letra... :") 
        u_pick = u_pick.lower() #Seguro contra MAYUS/Error.

        #Condicional para que no se repitan letras.
        if u_pick in letters_player:
            print("Ya elegiste esta letra, cámbiala...")
            continue

        letters_player.append(u_pick) #Por cada input se agrega a la var letters_player
        
        if u_pick in secret_word: #Si el input ingresado está en la palabra secreta...
            
            #Utilizamos la función creada antes para verificar cuantas veces se repite
            #el input ingresado por el jugador.

            indexes = list_duplicates_of(secret_word,u_pick)  
            
            #Creamos un BUCLE para ingresar el input del jugador en todas las posiciones en las que
            #se ha repetido.
            for e in indexes:                               
                secret_word_censure[e] = u_pick
            
            print(f"¡Correcto!, letras escritas: {letters_player}")
            
            secret_word_string = "".join(secret_word_censure)
            print(secret_word_string)

            if secret_word_censure == secret_word:
                print (f"¡Ganaste!, la palabra secreta es {secret_word_string}, letras escritas: {letters_player}")
                break        
            
        else: 
            
            print(f"¡Letra equivocada, ahora tienes {lives-1} vidas!, letras escritas: {letters_player}")
            lives -=1
            if lives == 0:
                print(f"¡Perdiste!, la palabra secreta era {secret_word_string_2}, letras escritas: {letters_player}, inténtalo de nuevo...")
                break
  
   
hangman()









