from Archivo import *

class Doc(Archivo):
    def __init__(self, nombre, tipo, tamaño):
        super().__init__(nombre,"DOC",tamaño)
    
    def mostrar(self):
        return(f"Nombre del Archivo: {self.nombre}\nTipo de Archivo: {self.tipo}\Tamaño del Archivo: {self.tamaño}")