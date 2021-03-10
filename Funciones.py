from Archivo import *
from Mov import *
from Doc import *
from Wav import *
from Pdf import *
from Carpeta import *

def mostrar_menu(menu):
    for i in menu:
        print(i.nombre)
        i.ver_contenido()

def validar_contenido_del_menu(menu, nombre):
    k = 0
    for i in menu:
        if i.nombre == nombre:
            print("La carpeta ya existe")
            k = 1
                
        while k == 1:

            nombre = input("Ingrese otro nombre: ")
            for i in menu:
                if i.nombre == nombre:
                    print("La carpeta ya existe")
                else:
                    k = 0

def agregar_carpeta_en_carpetaa(menu, folder, folder_name):
    for i in menu:
        print(folder_name)
        print(i.nombre)
        if (i.nombre) == folder_name:
            i.lista_archivos.append(folder)
            print(f"La carpeta {folder.nombre} se registró correctamente dentro de {i.nombre}")

def carpeta_en_menu(menu, folder_name, folder):
    for i in menu:
        if i.nombre == folder_name:
            agregar_carpeta_en_carpetaa(menu, folder, folder_name)
            print("aceptado")
            return True

def ver_carpeta(menu, accion):
    for i in menu:
        if i.nombre == accion:
            for l,j in enumerate(i.lista_archivos):
                print(f"{l+1}- {j.nombre}")


def marking(menu_principal, menu_archivos):
    k = 0
    nombre = input("\nIngrese el nombre de la carpeta/archivo al que desea acceder: ")

    while k == 0:
        for i in menu_principal:
            if i.nombre == nombre:
                ver_carpeta(menu_principal, nombre)
        k = 2

    while k == 2:
        for i in menu_archivos:
            if i.nombre == nombre:

                print(i.mostrar())
        k = 1

def carpeta_existente(menu, carpeta):
    for i in menu:
        if i.nombre == carpeta:
            return True
    return False
