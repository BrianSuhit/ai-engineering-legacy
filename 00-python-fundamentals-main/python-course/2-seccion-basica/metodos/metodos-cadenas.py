cadena_1 = "soy brian"

cadena_2 = "maquinola"

#devuelve la lista de atributos validos del objeto
dir(cadena_1)

#convierte a mayusculas
resultado = cadena_1.upper()

#convierte a minuscula
resultado = cadena_1.lower()

#primera en mayuscula
resultado = cadena_1.capitalize()

#primera letra de cada palabra en mayuscula
resultado = cadena_1.title()

#buscamos una cadena en otra cadena
busqueda_find = cadena_1.find("a")

#igual a find, pero si no encuentra nada, devuelve una excepcion
busqueda_find = cadena_1.index("a")

#si es numerico devuelve True
es_numerico = cadena_1.isnumeric()

#si es alfanumerico devuelve True, sino False ( A - Z)
es_alfanumerico = cadena_1.isalpha()

#devuelve la cantidad de coincidencias
contar_coincidencias = cadena_1.count()

#contamos cuantos caracteres tiene una cadena
contar_caracteres = cadena_1.len()

#es True si una cadena empieza con otra dada
empieza_con = cadena_1.startswith("soy")

#es True si una cadena termina con otra dada
termina_con = cadena_1.endswith("brian")

#reemplaza una parte de la cadena dada por otra
reemplazar = cadena_1.replace("brian", "lucas")

#separar cadenas con la cadena dada
separar = cadena_1.split()