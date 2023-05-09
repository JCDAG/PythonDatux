class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self):
        pais, lote, anio = self.codigo.split("-")
        return f"Producto: {self.nombre}, país de origen: {pais}, número de lote: {lote}"
        #   en caso queramos el año solo se tiene que agregar  return f"Producto: {self.nombre}, país de origen: {pais}, número de lote: {lote}, año {anio}"
producto1 = Producto("Sublime", "PERU-0001-2023")
print(producto1)
