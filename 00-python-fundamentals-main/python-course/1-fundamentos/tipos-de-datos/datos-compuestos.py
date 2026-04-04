#lista - se puede modificar
lista = ["brian suhit","ai engineering",True, 30]

#tupla - no se puede modificar
tupla = ("brian suhit","ai engineering",True, 30)

#esto es valido
lista[3] = "vivo"

#esto no es valido
tupla[3] = "vivo"

print(lista[3])


# CONJUNTO ( set )

#no se puede llamar a sus elementos por indice
#no almacena datos duplicados
#son datos desordenados
conjunto = {"brian suhit","ai engineering",True, 30}

print(conjunto)


# DICCIONARIO ( dict ) la estructura es key : value

diccionario = {
    "nombre" : "brian suhit",
    "trabajo" : "ai engineering",
    "edad" : 30,
    "vivo" : True
}

print(diccionario["edad"])