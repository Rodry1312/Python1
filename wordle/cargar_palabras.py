import unicodedata

def cargar_palabras_limpias(ruta_fichero:str="palabras_5.txt") -> list[str]:
    """
    Selecciona aleatoriamente la palabra del día de la lista de palabras.

    Parámetros:
        palabras (list): lista de palabras en mayúsculas

    Retorna:
        str: palabra seleccionada
    """
      
    def quitar_tildes(palabra: str) -> str:
        """Elimina los acentos y diéresis de una palabra."""
        return ''.join(
            c for c in unicodedata.normalize('NFD', palabra)
            if unicodedata.category(c) != 'Mn'
         )
    
    palabras_limpias=[]

    with open(ruta_fichero, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:  # ignora líneas vacías
                palabra = quitar_tildes(linea).upper()
                palabras_limpias.append(palabra)

    return palabras_limpias

if __name__ == "__main__":
    # --------------------------
    # Ejemplo de uso:
    palabras = cargar_palabras_limpias("palabras_5.txt")
    print(palabras[:20])  # muestra las primeras 20 palabras      