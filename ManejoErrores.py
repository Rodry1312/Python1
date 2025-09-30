nombre = input("Ingresa tu nombre: ")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print("Error: debes ingresar un numero válido")

while True:
    try:
        altura= float(input("Ingresa tu altura en metros: "))
        break
    except ValueError:
        print("Error debes ingresar un numero decimal para la altura")    


print(f"Hola {nombre}, tienes {edad} y mides {altura} metros")


print(f"El tipo de dato de 'nombre' es: {type(nombre)}") 
print(f"El tipo de dato de 'edad' es: {type(nombre)}") 
print(f"El tipo de dato de 'altura' es: {type(altura)}")

