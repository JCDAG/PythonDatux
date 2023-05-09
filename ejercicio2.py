class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_catalogo(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print(f"Descripción: {producto.descripcion}")
            print()
mi_catalogo = Catalogo()

while True:
    nombre = input("Ingresa el nombre del producto (o 'q' para salir): ")
    if nombre == 'q':
        break
    precio = float(input("Ingresa el precio del producto: "))
    descripcion = input("Ingresa una descripción del producto: ")
    nuevo_producto = Producto(nombre, precio, descripcion)
    mi_catalogo.agregar_producto(nuevo_producto)
print("Catálogo:")
mi_catalogo.mostrar_catalogo()
