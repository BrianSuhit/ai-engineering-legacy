#Una función Lambda es una Micro-Función Desechable

#sintaxis - lambda entrada : salida

numeros = [1, 2, 3, 4, 5, 6]

# filter( FUNCION, LISTA )
# Le paso una lambda que dice: "Devuelve True si el resto de dividir por 2 es 0"
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares) # [2, 4, 6]