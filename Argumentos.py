# main.py
import sys

def main():
    print("Argumentos recibidos:", sys.argv)

    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        if len(sys.argv) >= 4:
            edad = sys.argv[2]
            ciudad = sys.argv[3]
            print(f"Hola, {nombre} 👋. Tienes {edad} años y vives en {ciudad}. 🏙️")
        else:
            print(f"Hola, {nombre} 👋")
    else:
        print("No se proporcionó ningún argumento")


if __name__ == "__main__":
    main()
