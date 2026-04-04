diccionario = {
    "nombre": "brian",
    "apellido" : "suhit",
    "edad" : 30
}

#devuelve un objeto dict_item
claves = diccionario.keys()

#devuelve un objeto dict_value
valor = diccionario.values()

#obtiene un objeto con get () ( si no encuentra ninguno el programa sigue )
objeter_valor = diccionario.get("nombre")

#elimina todo del diccionario
diccionario.clear()

#elimina un objeto del diccionario
diccionario.pop("nombre")

#objetiendo un objeto dict_item iterable
diccionario_iterable = diccionario.items()