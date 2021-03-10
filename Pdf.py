from Archivo import *

class Pdf(Archivo):
    def __init__(self, nombre, tipo, tamaño):
        super().__init__(nombre,"PDF",tamaño)
    
    def mostrar(self):
        return(f"Nombre del Archivo: {self.nombre}\nTipo de Archivo: {self.tipo}\Tamaño del Archivo: {self.tamaño}")