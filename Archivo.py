class Archivo():
    def __init__(self, nombre, tipo, tamaño):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
    
    def mostrar_archivo(self):
        print(f'Nombre del archivo: {self.nombre} \n Tipo de archivo: {self.tipo} \n Tamaño del archivo: {self.tamaño}')