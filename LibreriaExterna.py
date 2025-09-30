import emoji

def calcular_imc_con_emoji(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
    elif imc < 25:
        estado = "Normal " + emoji.emojize(":smile:", language="alias")
    else:
        estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
    return imc, estado

# Ejemplo de uso:
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc, estado = calcular_imc_con_emoji(peso, altura)

print(f"Tu IMC es: {imc:.2f}")
print(f"Estado: {estado}")
