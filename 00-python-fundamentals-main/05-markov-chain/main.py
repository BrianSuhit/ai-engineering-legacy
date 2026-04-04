import random

class GeneradorDeTexto:
    """
    IA Generativa básica basada en Cadenas de Markov.
    Predice la siguiente palabra basándose en probabilidades aprendidas.
    """
    
    def __init__(self):
        # El cerebro es un diccionario: { "palabra_actual": ["opcion_A", "opcion_B"] }
        self.memoria = {}
        print(">>> IA Inicializada. Cerebro vacío esperando datos.")
        
    def entrenar(self, texto):
        """Procesa el texto y mapea las relaciones entre palabras consecutivas."""
        palabras = texto.split() # Tokenización
        
        # Recorremos el texto buscando pares (Bigramas)
        for i in range(len(palabras) - 1):
            palabra_actual = palabras[i]
            palabra_siguiente = palabras[i + 1]
            
            # Si la palabra es nueva, inicializamos su lista de opciones
            if palabra_actual not in self.memoria:
                self.memoria[palabra_actual] = []
                
            # Guardamos la 'siguiente' como una posibilidad futura
            self.memoria[palabra_actual].append(palabra_siguiente)
            
        print(f">>> Entrenamiento finalizado. Vocabulario: {len(self.memoria)} palabras base.")

    def predecir(self, inicio, max_palabras=10):
        """Genera una oración nueva navegando por las opciones aprendidas."""
        palabra_actual = inicio
        frase = [palabra_actual]
        
        print(f"Generando frase con semilla: '{inicio}'...")
        
        for _ in range(max_palabras):
            # Caso borde: Si la palabra no existe en memoria, dejamos de hablar
            if palabra_actual not in self.memoria:
                break
            
            # Lógica de Markov: Elegir aleatoriamente entre las opciones históricas
            opciones = self.memoria[palabra_actual]
            siguiente_palabra = random.choice(opciones)
            
            frase.append(siguiente_palabra)
            palabra_actual = siguiente_palabra # Avanzamos al siguiente estado
            
        texto_generado = " ".join(frase)
        print(f"🤖 DIJO: {texto_generado}")
        return texto_generado

# --- ZONA DE EJECUCIÓN ---

if __name__ == "__main__":
    # 1. Instanciamos el objeto
    mi_ia = GeneradorDeTexto()

    # 2. Datos de entrenamiento (Corpus)
    texto_entrenamiento = "el gato come pescado y el perro come carne pero el gato duerme en el sofa y el perro duerme en el patio"

    # 3. Entrenamos el modelo
    mi_ia.entrenar(texto_entrenamiento)
    print("-" * 30)

    # 4. Probamos la generación (Resultados estocásticos)
    mi_ia.predecir("el")