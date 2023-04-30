biblioteca = {
    "Comics": ["Civil War:Mark Millar", "La muerte de Superman: Dan Jurgens"],
    "Novelas": ["El Ingenioso Hidalgo Don Quijote de la Mancha:Miguel de Cervantes Saavedra", "Sherlock Holmes: Sir Arthur Conan Doyle", "Rayuela:JUlio Cortazar"],
    "Cuentos": ["Los tres cerditos:Joseph Jacobs", "Las mil y una noches:Anonimo", "Caperucita roja:Charles Perrault?", "Hanzel y Gretel:Hermanos Grimm"]
}

libros_prestados = []

usuarios = ["User-1", "User-2", "User-3"]

while True:
    print("1. Obtener lista de categorías de libros")
    print("2. Obtener nombres de los libros y autores")
    print("3. Cambiar estado de un libro a prestado")
    print("4. Lista de usuarios de la biblioteca")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        categorias = list(biblioteca.keys())
        print("Categorías de libros:")
        for categoria in categorias:
            print("- " + categoria)

    elif opcion == "2":
        print("Libros y autores:")
        for categoria in biblioteca:
            libros = biblioteca[categoria]
            for libro in libros:
                nombre, autor = libro.split(":") #Sirve para separar el nombre del autor
                print("- " + nombre + " (" + autor + ")")

    elif opcion == "3":
        libro = input("Ingrese el nombre del libro: ")
        if libro in libros_prestados:
            print("El libro ya ha sido prestado.")
        else:
            libros_prestados.append(libro)
            print("El libro ha sido marcado como prestado.")

    elif opcion == "4":
        print("Usuarios de la biblioteca:")
        for usuario in usuarios:
            print("- " + usuario)

    elif opcion == "5":
        break

    else:
        print("Opción inválida. Intente de nuevo.")
