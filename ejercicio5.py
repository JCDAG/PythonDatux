import os

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self):
        pais, lote, anio = self.codigo.split("-")
        return f"Producto: {self.nombre}, país de origen: {pais}, número de lote: {lote}"

try:
    producto1 = Producto("Sublime", "PERU/0001-2023") #se cambio un - por /
    print(producto1)
except ValueError:
    print("Error: el formato del código no es válido.")
else:
    print("Ruta del directorio de trabajo: ", os.getcwd())
finally:
    print("Proceso terminado.")
