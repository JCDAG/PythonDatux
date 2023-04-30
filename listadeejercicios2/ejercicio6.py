# 6.Crear una funcion Main que valide el ingreso para un evento , dividir esta funcion main en
# al menos 3 sub-funciones.
import datetime

def validar_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validar_lugar(lugar):
    lugares_validos = ['Hotel Sheraton']
    return lugar.lower() in lugares_validos

def validar_participante(participante):
    try:
        participante = int(participante)
        return participante > 0
    except ValueError:
        return False

def main():
    fecha=input("Ingresar la fecha del evento (DD/MM/AAAA)")
    if not validar_fecha(fecha):
        print("La fecha ingresada es invalida")
        return
    lugar=input("Ingrese el lugar")
    if not validar_lugar(lugar):
        print("El lugar es invalido")
        return
    participante=input("Ingrese el numero de participantes")
    if not validar_participante(participante):
        print("El número de participantes es inválido")
        return

    print("El evento ha sido validado correctamente")

main()
