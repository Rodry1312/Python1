# ejercicio7.py

def calcular_datos(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    return suma, promedio, maximo, minimo


def main():
    entrada = input("Introduce una lista de números separados por coma: ")
    try:
        numeros = [int(num.strip()) for num in entrada.split(",")]
        suma, promedio, maximo, minimo = calcular_datos(numeros)
        print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")
    except ValueError:
        print("⚠️ Error: asegúrate de introducir solo números separados por coma.")


if __name__ == "__main__":
    main()
