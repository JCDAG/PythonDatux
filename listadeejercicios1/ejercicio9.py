lista_python = []
lista_sql = []
lista_power_bi = []
print("Benvenido al menu")
while True:
    print("1. Agregar a la lista de Python")
    print("2. Agregar a la lista de SQL")
    print("3. Agregar a la lista de Power BI")
    print("4. Mostrar todas las listas")
   # print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        elemento = input("Ingrese un elemento para agregar a la lista de Python: ")
        lista_python.append(elemento)
        print("Elemento agregado a la lista de Python")
    elif opcion == 2:
        elemento = input("Ingrese un elemento para agregar a la lista de SQL: ")
        lista_sql.append(elemento)
        print("Elemento agregado a la lista de SQL")
    elif opcion == 3:
        elemento = input("Ingrese un elemento para agregar a la lista de Power BI: ")
        lista_power_bi.append(elemento)
        print("Elemento agregado a la lista de Power BI")
    elif opcion == 4:
        print("Lista de Python:", lista_python)
        print("Lista de SQL:", lista_sql)
        print("Lista de Power BI:", lista_power_bi)
        break
    else:
        print("Opción inválida")

print("Gracias por usar este programa")
