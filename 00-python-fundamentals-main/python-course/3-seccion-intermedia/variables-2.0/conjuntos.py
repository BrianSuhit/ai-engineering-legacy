#creando un conjunto con set()
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}


#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# conjunto 2 es un subconjunto? devuelve True o False
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#conjunto 1 es un superconjunto? devuelve True o False
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto2 > conjunto1

#verificamos si hay un numero en comun
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)