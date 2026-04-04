import csv

with open("python-course/4-seccion-semi-avanzada/archivos/csv/datos") as archivo:
   reader = csv.reader(archivo)
   for linea in reader:
      print(linea)