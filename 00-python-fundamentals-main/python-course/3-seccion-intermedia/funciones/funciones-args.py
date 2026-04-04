# MÁQUINA: Analizador de Sentimientos Masivo
# El asterisco * significa: "Agrupa todo lo que llegue en una tupla llamada 'frases'"
def detectar_spam(*frases):
    cantidad = len(frases)
    print(f"Recibí {cantidad} mensajes para analizar.")
    
    # Como 'frases' es una lista (tupla), puedo recorrerla
    for frase in frases:
        if "gratis" in frase:
            print(f"ALERTA SPAM: {frase}")
        else:
            print(f"Mensaje limpio: {frase}")

# Puedo tirarle 1, 3 o 50 argumentos, la máquina no se rompe
detectar_spam("Hola Brian", "Gana dinero gratis", "Reunión mañana")