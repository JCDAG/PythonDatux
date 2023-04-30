while True:
    print("1. Imprimir cuadrado de asteriscos")
    print("2. Multiplos de 2")
    print("3. Listas")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        m = int(input("Cantidad de asteriscos del cuadrado: "))
        n = m
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                print("*", end="")
                
            print("")
    elif opcion == "2":
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for numero in numeros:
            if numero % 2 == 0:
                print(numero)
    elif opcion == "3":
        personas = [
             {"nombre": "Juan", "edad": 25},
             {"nombre": "María", "edad": 17},
             {"nombre": "Pedro", "edad": 30},
             {"nombre": "Laura", "edad": 16},
             {"nombre": "Ana", "edad": 18}
        ]

        for persona in personas:
            if persona["edad"] >= 18:
                print(persona["nombre"] + " es mayor de edad")

    elif opcion == "4":
        break

    else:
        print("Opción inválida. Intente de nuevo.")


