def presentarPersona (nombre="Usuario", edad = None, *aficiones):
    if edad is not None:
        mensaje = f"{nombre} tiene {edad} años "
    else:
        mensaje = f"{nombre} (edad no especificada)"

    if aficiones:
        hobbies = ", ".join(aficiones)
        mensaje += f" y le gusta: {hobbies}"


    print(mensaje) 

presentarPersona("Ana ", 25, "leer", "correr", "viajar")
presentarPersona("Luis", 30, "programar")
presentarPersona("Marta", 22)
presentarPersona()
