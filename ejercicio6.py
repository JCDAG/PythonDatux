class Pelicula:
    def __init__(self,titulo,duracion,release) -> None:
        self.titulo=titulo
        self.duracion=duracion
        self.release=release
    def __str__(self) -> str:
        return f"{self.titulo} se estreno el {self.release} y dura {self.duracion} minutos"

class Catalogo:
    listaPeliculas=[]
    def __init__(self) -> None:
        self.name="Catalogo Peliculas"
        self.listaPeliculas=[]
    def agregar(self, x):  # p será un objeto Pelicula
        self.listaPeliculas.append(x)
    def mostrar(self):
        for iterador in self.listaPeliculas:
            print(iterador)  # Print toma por defecto str(p)
    def filtroDuracion(self,duracion=0):
        resultadoFiltro=[]
        for iteradorPelicula in self.listaPeliculas:
            if iteradorPelicula.duracion>duracion:
                resultadoFiltro.append(iteradorPelicula)
        return resultadoFiltro
    def filtroAnio(self, anio=0):
        resultadoFiltro=[]
        for iteradorPelicula in self.listaPeliculas:
            if iteradorPelicula.release == anio:
                resultadoFiltro.append(iteradorPelicula)
        return resultadoFiltro

    def filtroMenos90Min(self):
        resultadoFiltro=[]
        for iteradorPelicula in self.listaPeliculas:
            if iteradorPelicula.duracion < 90:
                resultadoFiltro.append(iteradorPelicula)
        return resultadoFiltro
    ## añadir filtro de release segun un año espeficio
    
peli1=Pelicula("ant man",120,2020)
peli2=Pelicula("mario b",80,2023)

c1=Catalogo()
c1.agregar(peli1)
c1.agregar(peli2)
c1.mostrar()
print("Películas de menos de 90 minutos:")
resultado_filtro = c1.filtroMenos90Min()
for pelicula in resultado_filtro:
    print(pelicula)

print("Películas del año 2020:")
resultado_filtro = c1.filtroAnio(2020)
for pelicula in resultado_filtro:
    print(pelicula)