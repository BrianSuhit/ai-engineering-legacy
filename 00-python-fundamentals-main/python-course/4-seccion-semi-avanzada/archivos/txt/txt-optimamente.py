#abriendo el archivo con with open
with open("python-course/4-seccion-semi-avanzada/archivos/metas") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    print(contenido)
