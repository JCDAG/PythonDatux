# Almacenar la contraseña en una variable
contraseña = "73450209"

# Preguntar al usuario por la contraseña
contraseña_usuario = input("Introduce la contraseña: ")

# Comparar las contraseñas sin tener en cuenta mayúsculas y minúsculas
if contraseña.lower() == contraseña_usuario.lower():
    print("¡Contraseña correcta!")
else:
    print("Contraseña incorrecta.")
