#10. Defina una lista de DNI's y otra lista de datos que tenga lista anidadas en donde
# si la posición del DNI es x la información se encuentra en la posición x de la lista de
# datos, pedir datos para validar si el usuario tiene permitido ingresar , validar que
# exista en la lista de dni , que su edad sea mayor a 18 años y que sea datux en el curso de python.
# Ejemplo : [ 'name', edad,'distrito','datux','curso:sql']


dni_list = ['73450209', '25798952', '73450207', '09621898'] #Definimos la lista de DNIs
info_list = [['Julio', 18, 'Los Olivos', True, 'Python'], 
             ['María', 20, 'Independencia', False, 'SQL'], 
             ['Pedro', 30, 'Comas', True, 'Python'], 
             ['Lucía', 19, 'San Juan de Lurigancho', True, 'Python']]
# Pedimos el DNI del usuario y verificamos si está en la lista
dni = input("Ingrese su DNI: ")
if dni in dni_list:
    # Obtenemos la posición del DNI en la lista
    index = dni_list.index(dni)
    # Obtenemos la información del usuario
    info = info_list[index]
    # Verificamos si el usuario tiene permitido ingresar
    if info[1] >= 18 and info[3] and info[4] == 'Python':
        # El usuario cumple con los requisitos, podemos permitir el ingreso
        print("Bienvenido/a,", info[0])
    else:
        # El usuario no cumple con los requisitos
        print("Lo siento, no tiene permitido el ingreso")
else:
    # El DNI ingresado no está en la lista
    print("El DNI ingresado no está registrado") 
