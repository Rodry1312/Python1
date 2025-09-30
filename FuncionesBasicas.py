def saludar(nombre):
    return f"Hola {nombre}, ¡BINEVENIDO/A! "

def calcular_imc(peso, altura):
    return peso/ (altura ** 2)

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura: "))
peso = float(input("Ingrese tu peso: "))

mensaje = saludar(nombre)
imc = calcular_imc(peso,altura)

print(mensaje)
print(f"{nombre}, tienes {edad}, mides {altura} m y pesas {peso} kg")
print(f"Tu IMC es: {imc:.2f}")