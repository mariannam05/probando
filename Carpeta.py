class Carpeta():
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_archivos = []
    
    def mostrar_carpeta(self):
        print(f'Nombre de la carpeta: {self.nombre} \n Archivos de la carpeta: {self.lista_archivos}')
    
    def ver_contenido(self):
        for i in self.lista_archivos:
            print(i.nombre)

    def nombre_carpeta(self):
        print(f"Carpeta: {self.nombre}")