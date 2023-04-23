#4.Ingrese un valor e imprima el tipo de dato.
valor = input("Ingrese un valor: ")
if "." in valor:
        valor_float = float(valor)
        print("El tipo de dato del valor ingresado es:", type(valor_float))
else:
        valor_int = int(valor)
        print("El tipo de dato del valor ingresado es:", type(valor_int))

