import os
print(f"Estoy parado en: {os.getcwd()}") 

archivo_sin_leer = open("python-course/4-seccion-semi-avanzada/archivos/metas", encoding="UTF-8")

#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()

#cerramos el archivo
archivo_sin_leer.close()


print(linea)