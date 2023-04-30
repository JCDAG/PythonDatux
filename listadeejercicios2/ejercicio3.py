# 3. Definir una función que retorne el mayor valor al ingresar 2 números.
x=int(input("ingresa tu primer numero: "))
y=int(input("ingrese el segundo numero: "))
def mayor(x,y):
     if x>y:
         print(str(x)+ ' es mayor que '+str(y))
     else:
        print(str(y)+ ' es mayor que '+ str(x))
mayor(x, y)