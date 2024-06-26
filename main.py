import json

def abrir_archivo():
    with open("biblioteca.json", mode="r") as archivoJson:
        leer = json.load(archivoJson)
    return leer

def buscar_autores():
    abrir = abrir_archivo()
    autores = abrir["Autor"]

    for autor in (autores):
        print("Nombre: ",autor["Nombre"])
        print("Nacionalidad: ",autor["Nacionalidad"])

def editar_autor(id, nombre, nacio):
    abrir = abrir_archivo()
    autores = abrir["Autor"]

    autor_l = None
    
    for i, autor in enumerate(autores):
        if autor["AutorID"] == id:
            autor_l = autor
    
    if autor_l is not None:
        autor_l["Nombre"] = nombre
        autor_l["Nacionalidad"] = nacio
    
    with open("biblioteca.json", mode="w") as archivoJson:
        json.dump(abrir, archivoJson, indent=4)

def eliminar_autor(id:int):
    abrir = abrir_archivo()
    autores = abrir["Autor"]

    indice = None

    for i, autor in enumerate(autores):
        if autor["AutorID"] == id:
            indice = i
    
    if indice is not None:
        autores.pop(indice)
    
    with open("biblioteca.json", mode="w") as archivoJson:
        json.dump(abrir, archivoJson, indent=4)

def agregar_autor(nombre:str, nacionalidad:str):
    abrir = abrir_archivo()
    autores = abrir["Autor"]

    nuevo = {
        "AutorID": len(autores)+1,
        "Nombre": nombre,
        "Nacionalidad": nacionalidad
    }

    autores.append(nuevo)

    with open("biblioteca.json", mode="w") as archivoJson:
        json.dump(abrir, archivoJson, indent=4)