import json

def abrir_archivo():
    with open("biblioteca.json", mode="r") as archivoJson:
        leer = json.load(archivoJson)
    return leer

def crear_reporte():
    contador = 0
    abrir = abrir_archivo()

    n_autor = None
    for autor in abrir["Autor"]:
        id = autor["AutorID"]
    
    for prestamo in abrir["Prestamo"]:
        continue

# No pude con el reporte