import sys

# OPCIÓN A: Traer toda la caja
import operaciones

resultado = operaciones.sumar(5, 5) # Tengo que decir "NombreCaja.Herramienta"

# OPCIÓN B (Más usada): Sacar solo lo que necesito
from operaciones import sumar

resultado = sumar(5, 5) # Uso la herramienta directo


# ENRUTAMIENTO

# from CARPETA.ARCHIVO import FUNCION
from enrutamiento.matematicas import sumar

print(sumar(2, 2))


# "Oye Python, agrega esta ruta a tu mapa de búsqueda"
sys.path.append("/home/brian/documentos/mis_modulos_secretos")

# Ahora sí lo encuentra
#import modulo_secreto