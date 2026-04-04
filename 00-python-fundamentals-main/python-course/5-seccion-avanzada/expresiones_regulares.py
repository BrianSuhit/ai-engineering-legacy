import re

texto = ''' hola maestro, esta es la cadena 1, como estas mi capitan
    Esta es la linea 2 de texto
    Y esta es la linea 3 de texto, la ultima'''
    
#haciendo una busqueda simple
resultado = re.findall("esta", texto)

#haciendo una busqueda sin tener en cuenta mayuscula
resultado = re.findall("esta", texto, re.IGNORECASE)

#busqueda de digitos numericos ( 0 - 9 )
resultado = re.findall(r"\d", texto)

#busqueda de todo MENOS digitos numericos
resultado = re.findall(r"\D", texto)

#busqueda de todo caracteres alfanumericos ( a - z, A - Z, 0 - 9, _ )
resultado = re.findall(r"\w", texto)

#busqueda de todo MENOS caracteres alfanumericos
resultado = re.findall(r"\W", texto)

#busqueda de espacios en blanco, tabs, saltos de linea
resultado = re.findall(r"\s", texto)

#busqueda de todo MENOS espacios en blanco, tabs, saltos de linea
resultado = re.findall(r"\S", texto)

#busqueda de saltos de linea
resultado = re.findall(r'\n', texto)

#busqueda de todo MENOS saltos de linea
resultado = re.findall(r'.', texto)

#cancelar caracteres especiales
resultado = re.findall(r'\.', texto)

#busca el comienzo de una linea ( acento circunflejo )
resultado = re.findall(r'^hola', texto, re.MULTILINE)

#busca el final de una linea
resultado = re.findall(r'capitan$', texto, re.MULTILINE)

#busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}', texto)

#busca minimo n, maximo m
resultado = re.findall(r'\d{1,3}', texto)