#creando diccionario con dict

diccionario = dict(nombre="brian",apellido="suhit",edad=30)

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dato1","dato2"]):"valor1"}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","edad"])