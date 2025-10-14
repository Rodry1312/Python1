import random
import cargar_palabras
GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
GRAY_BG = "\033[47m"
RESET = "\033[0m"

def colorearLetra(letra:str,estado:str) -> str :

    """ 
    La función recive una letra y y un estado de la letra y  
    devuelve la letra coloreada 
    """

    if(estado=="verde"):

        return f"{GREEN_BG} {letra.upper()} {RESET}"

    elif(estado=="amarillo"):

        return f"{YELLOW_BG} {letra.upper()} {RESET}"

    else:

        return f"{GRAY_BG} {letra.upper()} {RESET}"

    
def elegir_palabra(palabras:list[str]) -> str:
    """
    Selecciona aleatoriamente la palabra del día de la lista de palabras.

    Parámetros:
        palabras (list): lista de palabras en mayúsculas

    Retorna:
        str: palabra seleccionada
    """
    
    random_index=random.randint(0,len(palabras))
    palabra=palabras[random_index]

    return palabra


def comprobarIntento(palabraSecreta:str,intento:str):
    """
    Compara el intento con la palabra secreta y 
    devuelve una lista indicando
    para cada letra si es:
        - "verde" -> letra correcta y en la posición correcta
        - "amarillo" -> letra presente en otra posición
        - "gris" -> letra no presente

    Parámetros:
        palabra_secreta (str): palabra a adivinar
        intento (str): intento del jugador

    Retorna:
        list[str]: lista de estados por letra
    """

    letras_palabra_secreta=list(palabraSecreta.upper())

    letras_intento=list(intento.upper())

    estados=[]
    
    for i in range(len(letras_intento)):
        esta=False
        if(letras_palabra_secreta[i]==letras_intento[i]):
            estados.append("verde")
            esta=True
        for a in range(len(letras_intento)):
            if(letras_intento[i] == letras_palabra_secreta[a] and not esta):
                estados.append("amarillo")
                esta=True
        
        if(not esta):
                estados.append("gris")
                esta=True


    return estados

def mostrar_feedback(intento,resultado):

    letras=list(intento)

    letras_coloreadas=[]

    for i in range(len(letras)):
        print(colorearLetra(letras[i],resultado[i]) ,end="")






