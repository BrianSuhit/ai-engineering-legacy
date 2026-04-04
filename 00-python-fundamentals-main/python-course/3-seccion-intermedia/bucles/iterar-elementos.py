
animales = ["gato", "perro", "cocodrilo"]

numeros = [10,20,30,40,50]

#recorriendo la lista animes
for animal in animales:
    print(f"Ahora la variable animal es igual a {animal}")
    
#recorriendo la lista numeros y haciendo una multiplicacion
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#for aninado convencional
for anima in animales:
    for numero in numeros:
        print(anima,numero)
        
#for aninado de python ( las listas deben tener el mismo tamaño )
for numero,animal in zip(numeros,animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    

#forma de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#usando else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
    
# TODO LO ANTERIOR FUNCIONA IGUAL PARA TUPLAS Y CONJUNTOS