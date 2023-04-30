# 4. Definir una función que imprima los argumentos ingresados desde línea de comandos
# Nota: Usar import sys.argv => *args
import sys
op=int(input("Ingresa la cantidad de argumentos: "))
lista=[]
def ingreso(op):
    for x in range(0,op):
        lista.append(input(f"El argumento numero {x+1} es: "))
    return lista

def imprimirArgumentos(*args):
    for arg in args:
        print(arg)