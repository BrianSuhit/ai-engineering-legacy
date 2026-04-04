frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

#utilizando continue para saltar iteracion
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"me voy a comer una fruta: {fruta}")
    
    
#utilizando break para romper bucle
for fruta in frutas:
    print(f"me voy a comer una fruta: {fruta}")
    if fruta == "pera":
        break

print("bucle terminado")


#recorriendo una cadena de texto

cadena = "hola me llamo brian y soy ai engineering"

for letra in cadena:
    print(letra)
    

#for en una sola linea de codigo
numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)