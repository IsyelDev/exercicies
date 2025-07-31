class Pelicula:
    def __init__(self, titulo: str, duracion: int, lanzamiento: int):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

    def __str__(self):
        return f'{self.titulo} ({self.lanzamiento})'


class Catalogo:
    def __init__(self, peliculas=None):
        self.peliculas = peliculas if peliculas else []

    def agregar(self, p: Pelicula):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)


# Entrada de datos
titulo = input("Título: ")
duracion = int(input("Duración (min): "))
lanzamiento = int(input("Año de lanzamiento: "))

# Crear película y catálogo
p = Pelicula(titulo, duracion, lanzamiento)
c = Catalogo([p])

# Mostrar catálogo
print("\nPelículas en catálogo:")
c.mostrar()
