import division

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Dividir dos números")
    print("2. Salir")

while True:
    mostrar_menu()
    opcion = input()

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = operaciones.dividir(num1, num2)
        print(f"El resultado es: {resultado}")
    elif opcion == "2":
        break
    else:
        print("Opción inválida")