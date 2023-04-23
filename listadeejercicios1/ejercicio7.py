#7. Realiza un programa que lea 2 números por teclado y determine los siguientes
#aspectos:
#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero
n=int(input("Ingrese el primer numero:"))
m=int(input("Ingrese el segundo numero:"))
if n==m:
    print("Los numeros ", n ,"y", m, "son iguales")
else:
        print("Los numeros ", n ,"y", m, "son diferentes")
if n>m:
        print("El primer numero ", n ,"es mayor que el segundo", m)
else:
        print("El segundo número", m ,"es mayor o igual que el primero", n)


