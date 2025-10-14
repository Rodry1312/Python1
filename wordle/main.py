import cargar_palabras
import wordle_funciones
import math

palabra = wordle_funciones.elegir_palabra(cargar_palabras.cargar_palabras_limpias())
bandera=False
intentos=6
estados=[]
while not bandera:
    print(f"\nIntento {intentos}")

    respuesta=input("Introduce una palabra:")

  
    if len(respuesta) != 5 :
        print("Palabra con longitud distinta a 5")
        continue
   
    else:
       estados= wordle_funciones.comprobarIntento(palabra,respuesta)

    wordle_funciones.mostrar_feedback(respuesta,estados)

    if(estados==["verde","verde","verde","verde","verde"] or intentos==1):
        bandera=True
        print(f"La palabra secreta era {palabra}")

    intentos=intentos-1
