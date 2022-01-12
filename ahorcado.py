from palabrasAhorcado import lista_palabras
#importamos un elemento de un archivo especifico
import random
#importamos toda una libreria
import string
from diagrama import vidas_diccionario_visual 



def obtener_palabras_validas(lista_palabras):
    palabra = random.choice(lista_palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(lista_palabras)    
    return palabra.upper()

#upper convierte los caracteres en mayuscula y la funcion saca el guion
#y los espacios  

def ahorcado ():
    
    print ("\n¡Que comience el Juego!")
    print("\n")
    nombre = input("Ingresa tu nombre: ")
    print(f"¡Bienvenide {nombre}!")



    palabra = obtener_palabras_validas(lista_palabras)

    letra_por_adivinar = set(palabra)
    #separa las palabras en letras (hace un conjunto)
    abecedario = set(string.ascii_uppercase)
    letras_adivinadas = set()

    vidas = 7

    while len(letra_por_adivinar) > 0 and vidas > 0:
        if vidas == 7 and letras_adivinadas == set() :
            print (f"Tines {vidas} vidas, cuidalas bien")
        else:
            print (f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
            palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
            #mostras estado ahoracaro.
            print(vidas_diccionario_visual[vidas])
            #mostrar letras por separas por un espacio.
            print(f"Palabra:{' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add (letra_usuario)
            
            #Si la letra esta en la palabra
            #quitar la letra del conjunto de letras
            #pendientes por adivnar
            #si no esta en la palabra, quitar una vida

            if letra_usuario in letra_por_adivinar:
                letra_por_adivinar.remove (letra_usuario)
                print('')
            # Si la letra no está en la palabra, quitar una vida.
            else:   
                vidas = vidas-1
                print (f"\nLa Letra,{letra_usuario} no esta en la palabra. ")
            #si la letra escogida por el usuario ya fue ingresada        
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva")
        else:
            print("\nEsta letra no es valida. ")
    # El juego llega a esta línea cuando se agotan las vidas del jugador 
    # o cuando se adivinan todas las letras de la palabra.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra era {palabra}!')

if __name__ == '__main__':
    ahorcado()  



 






