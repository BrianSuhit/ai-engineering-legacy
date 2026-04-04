#creando mi propia excepcion personalizada

class MiExcepcion(Exception):
    def __init__(self, mensaje):
        print(f"cometiste el siguiente error: {mensaje}")
        
        
#lanzando mi propia excepcion
try:
    raise MiExcepcion("veo que alguien no leyo la documentacion")
except:
    print("¿como vas a cometer ese error?")