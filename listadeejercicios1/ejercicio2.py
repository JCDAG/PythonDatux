#2.Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el teclado.
#En este ejercicio puse separado el imput del float, en los otros se usa la estructura float(input())
radio=input("Ingrese el radio:")
radio=float(radio)
pi=3.14
areacirculo=pi*radio**2
print(areacirculo)
altura=input("Ingrese el altura del triangulo:")
altura=float(altura)
base=input("Ingrese la base del triangulo:")
base=float(base)
areatriangulo=(base*altura)/2
print(areatriangulo)
lado=input("Ingrese la medida de lado del cuadrado:")
lado=float(lado)
areacuadrado=lado**2
print(areacuadrado)