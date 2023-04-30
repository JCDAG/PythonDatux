# 5.Crear una funcion que al mandar como parámetro un path me liste los elementos que
# contiene esa carpeta ,en caso sea una carpeta llamar otra vez tu función que lista los
# elementos de esa subcarpeta.
import os
def listarElementos(path):
     elementos=os.listdir(path)
     for elemento in elementos:
        print(elemento)
        if os.path.isdir((os.path.join(path, elemento))):
            listarElementos(os.path.join(path, elemento))
            #('C:\Users\USUARIO.DESKTOP-9DIO54H\Escritorio\workspacedatux\PythonDatux\listadeejercicios2')
            