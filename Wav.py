from Archivo import *

class Wav(Archivo):
    def __init__(self, nombre, tipo, tamaño):
        super().__init__(nombre,"WAV",tamaño)
    
    def mostrar(self):
        return(f"Nombre del Archivo: {self.nombre}\nTipo de Archivo: {self.tipo}\Tamaño del Archivo: {self.tamaño}")