from Archivo import *
from Mov import *
from Doc import *
from Wav import *
from Pdf import *
from Carpeta import *
from Funciones import *



menu = []
menu_principal = []
menu_archivos = []
print("Bienvenido al Drive X")

while True:
    
    accion = input('''\nIndique qué acción desea realizar:\n
    1- Crear una carpeta
    2- Crear un archivo
    3- Eliminar un archivo
    4- Eliminar una carpeta
    5- Mostrar archivos y carpetas
    6- Ordenar archivos
    ==> ''')

    while not (accion == "1" or  accion == "2" or  accion == "3" or  accion == "4" or  accion == "5" or  accion == "6" ):
        accion = input("Ingreso inválido. Seleccione una opción válida")

    if accion == "1":           #crear carpeta
        nombre = input("\nIngrese el nombre de la carpeta a crear: ")
        validar_contenido_del_menu(menu,nombre)

        folder = Carpeta(nombre)
        menu.append(folder)
        accion = input('''\nIndique dónde desea agregar la carpeta: \n
    1- Menu principal
    2- Dentro de una carpeta:
    => ''')
        
        if accion == "1":           #dentro del menu principal
            menu_principal.append(folder)
        else:                          #dentro de una carpeta
            folder_name = input(f"Ingrese el nombre de la carpeta donde desea guardar {folder.nombre}: (NOTA: debió haberla creado anteriormente) ")
            variable = False
            variable = carpeta_en_menu(menu, folder_name, folder)
            while not variable:
                folder_name = input(f"La carpeta que ingresó no existe. Seleccione el nombre de la carpeta donde desea guardar {folder.nombre}: ")
                variable = carpeta_en_menu(menu, folder_name, folder)
                
    elif accion == "2":             #crear un archivo
        if int(len(menu)) == 0:
           print("\nAún no hay carpetas registradas")
        else:
            nombre = input("Nombre del archivo que desea crear: ")
            tamaño = input("Tamaño del archivo que desea crear: ")
            tipo = input('''Tipo de archivo: 
    1- .DOC
    2- .MOV
    3- .WAV
    4- .PDF
    ==> ''')
            while not (tipo == "1" or tipo == "2" or tipo == "3" or tipo == "4"):
                tipo = input("Ingreso inválido, seleccione un tipo de archivo correcto: ")
            if tipo == "1":
                documento = Doc(nombre, "DOC", tamaño)
            elif tipo == "2":
                documento = Mov(nombre, "MOV", tamaño)
            elif tipo == "3":
                documento = Wav(nombre, "WAV", tamaño)
            else:
                documento = Pdf(nombre, "PDF", tamaño)

            carpeta = input(f"\nIngrese el nombre de la carpeta donde desea guardar {documento.nombre}: ")
            bolean = carpeta_existente(menu, carpeta)
            while not bolean:
                carpeta = input(f"\nCarpeta no existente. Ingrese el nombre de la carpeta donde desea guardar {documento.nombre}: ")
                bolean = carpeta_existente(menu, carpeta)
            for i in menu:
                if i.nombre == carpeta:
                    i.lista_archivos.append(documento)
            menu_archivos.append(documento)
            print(f"{documento.nombre} se guardó existosamente en {carpeta}")

    elif accion == "3":             #eliminar un archivo
        k = 0
        nombre = input("\nIndique el nombre del archivo que desea borrar: ")

        for j,i in enumerate(menu_archivos):
            if i.nombre == nombre:
                k = 1
                h = j

        while not k == 1:
            nombre = input("\nIngreso inválido. Indique el nombre del archivo que desea borrar: ")
            for j,i in enumerate(menu_archivos):
                if i.nombre == nombre:
                    k = 1
                    h = j
        menu_archivos.pop(h)
        for i in menu:
            for m,j in enumerate(i.lista_archivos):
    
                print(j.nombre)
                if nombre == j.nombre:
                    i.lista_archivos.pop(m)
        print(menu_archivos)

    elif accion == "4":             #eliminar una carpeta
        k = 0
        while k == 0:
            carpeta = input("Ingrese el nombre de la carpeta que desea borrar: ")
            for i,j in enumerate(menu):
                if j.nombre == carpeta:
                    menu.pop(i)
                    
                    k = 1
                    for t,p in enumerate(j.lista_archivos):
                        for w,k in enumerate(menu):
                        
                            if p.nombre == k.nombre:
                                j.lista_archivos.pop(t)
                                menu.pop(w)
                    for t,p in enumerate(j.lista_archivos):
                        for w,k in enumerate(menu_archivos):
                        
                            if p.nombre == k.nombre:
                                j.lista_archivos.pop(t)
                                menu_archivos.pop(w)
                    for t,p in enumerate(menu_principal):
                        if p.nombre == carpeta:
                            menu_principal.pop(t)
            if k == 0:
                k = input("Ingreso inválido. Presione 0 si desea eliminar una carpeta o 1 si desea salir de este apartado: ")
        
    elif accion == "5":         #mostrar archivos y carpetas
        if int(len(menu)) == 0:
            print("Aún no se han creado carpetas")
        else:
            print("\n-----Menú Principal-----\n")
            for i,j in enumerate(menu_principal):
                print(f"{i+1}- {j.nombre}")
            
            marking(menu_principal, menu_archivos)
            
            while True:
                eleccion = input("\n¿Desea acceder a otra carpeta?\n1- Si\n2- No\n==>")
                while not ( eleccion =="1" or eleccion =="2"):
                    eleccion = input("\nOpción inválida, selecciona una opción correcta: ")
                if eleccion == "2":
                    break
                else:
                    marking(menu, menu_archivos)

    else: 
        #falta ordenar archivos 
    otro = input("\n¿Desea realizar alguna otra operación?('S' para 'sí', 'N' para 'no'): ")
    while (otro.upper() != 'S') and (otro.upper() != 'N'):
        otro = input("Por favor ingrese un valor válido: ")
    if otro.upper() == "S":
        continue
    else:
        break
                 
                    