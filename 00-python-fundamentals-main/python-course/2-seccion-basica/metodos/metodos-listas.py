#List crea una lista
lista = list(["brian suhit", 30, "ai engineering"])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJA")

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "jajaja")

#agregando varios elementos a la lista
lista.extend([False, 2030])

#eliminando un elemento de la lista ( por su indice )
lista.pop(0)

#remueve un elemento por su valor
lista.remove("JAJAJA")

#elimina todo
lista.clear()

#ordena la lista
lista.sort()
lista.sort(reverse=True)

#invierte los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index("brian suhit")


print(lista)