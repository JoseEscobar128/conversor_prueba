from colorama import Fore, Style, init

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def pesos_a_dolares(pesos, tasa=18.5):
    return pesos / tasa

def dolares_a_pesos(dolares, tasa=18.5):
    return dolares * tasa

def main():
    init(autoreset=True)
    print(Fore.CYAN + "=== Conversor de Temperaturas y Monedas ===")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Pesos → Dólares")
    print("4. Dólares → Pesos")
    
    opcion = input(Fore.YELLOW + "Selecciona una opción: ")

    if opcion == "1":
        c = float(input("Introduce grados Celsius: "))
        print(f"{c} °C = {celsius_a_fahrenheit(c):.2f} °F")
    elif opcion == "2":
        f = float(input("Introduce grados Fahrenheit: "))
        print(f"{f} °F = {fahrenheit_a_celsius(f):.2f} °C")
    elif opcion == "3":
        p = float(input("Introduce cantidad en pesos: "))
        print(f"${p} MXN = ${pesos_a_dolares(p):.2f} USD")
    elif opcion == "4":
        d = float(input("Introduce cantidad en dólares: "))
        print(f"${d} USD = ${dolares_a_pesos(d):.2f} MXN")
    else:
        print(Fore.RED + "Opción no válida.")

if __name__ == "__main__":
    main()
