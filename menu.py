import json, main

print("Mundo LIBRO")
print("1. Mantenedores de Autores")
print("2. Reportes")
print("3. Salir")
opc = int(input("Ingrese la opción en el menú: "))
while True:
    match opc:
        case 1:
            print("Mantenedores Autores")
            print("1. Agregar Autores")
            print("2. Editar Autores")
            print("3. Eliminar Autores")
            print("4. Buscar Autor")
            print("5. Volver")
            a = int(input("Ingrese una opción en el menú: "))
            match a:
                case 1:
                    nom = input("Ingrese el nombre del autor: ")
                    nacio = input("Ingrese el nacionalidad del autor: ")
                    main.agregar_autor(nom,nacio)
                    break
                case 2:
                    ida = int(input("Ingrese el ID de un autor para editar: "))
                    nombre = input("Ingrese el nuevo nombre: ")
                    nacionalidad = input("Ingrese la nacionalidad: ")
                    main.editar_autor(ida, nombre, nacionalidad)
                case 3:
                    ida = int(input("Ingrese el ID del autor que quiere eliminar: "))
                    main.eliminar_autor(ida)
                case 4:
                    main.buscar_autores()
        case 2:
            continue # no pude el reporte :(
        case 3:
            break