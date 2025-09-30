# calculadora.py
import sys

def mostrar_ayuda():
    print("Uso: python calculadora.py <num1> <operador> <num2>")
    print("Ejemplos:")
    print("  python calculadora.py 5 + 3")
    print("  python calculadora.py 10 * 4")

def main():
    if len(sys.argv) != 4:
        print("⚠️ Error: número de argumentos incorrecto.")
        mostrar_ayuda()
        return

    try:
        num1 = float(sys.argv[1])
        operador = sys.argv[2]
        num2 = float(sys.argv[3])
    except ValueError:
        print("⚠️ Error: los números deben ser válidos.")
        mostrar_ayuda()
        return

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("🚫 Error: división entre cero.")
            return
        resultado = num1 / num2
    else:
        print(f"⚠️ Operador '{operador}' no reconocido. Usa +, -, * o /.")
        return

    print(f"✅ Resultado: {num1} {operador} {num2} = {resultado}")


if __name__ == "__main__":
    main()
