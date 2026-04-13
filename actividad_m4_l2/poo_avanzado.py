class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

class Libro:
    def __init__(self, titulo, autor, anio_publicacion, nombre_editorial, ciudad_editorial):
        self.titulo = titulo
        self.autor = autor  
        self.anio_publicacion = anio_publicacion
        
        self.editorial = Editorial(nombre_editorial, ciudad_editorial)

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.nombre} ({self.autor.pais})")
        print(f"Año: {self.anio_publicacion}")
        print(f"Editorial: {self.editorial.nombre} ({self.editorial.ciudad})")

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_anio_publicacion(self):
        return self.anio_publicacion

    def set_anio_publicacion(self, nuevo_anio):
        self.anio_publicacion = nuevo_anio

    def resumen(self, texto=None):
        if texto is None:
            print("Libro sin resumen disponible")
        else:
            print(f"Resumen: {texto}")


autor1 = Autor("Gabriel García Márquez", "Colombia")

libro1 = Libro( "100 años de soledad", autor1, 1967, "Sudamericana", "Buenos Aires")

libro1.mostrar_info()

print("\n--- Modificando título ---")
libro1.set_titulo("Cien años de soledad")
print(libro1.get_titulo())

print("\n--- Resumen ---")
libro1.resumen()
libro1.resumen("Una historia sobre la familia Buendía en Macondo.")