diccionario = {
    "nombre" : "brian",
    "apellido" : "suhit"
}

#recorriendo diccionario para obtener clave
for key in diccionario:
    print(f"la clave es: {key}")
    
#recorriendo diccionario para obtener value
for value in diccionario.values():
    print(f"el valor es: {value}")
    
#recorriendo diccionario para obtener clave y value
for key,value in diccionario.items():
    print(f"la clave es: {key} y el valor es: {value}")