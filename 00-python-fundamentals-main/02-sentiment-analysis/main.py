# Base de Conocimiento (Lexicon)
# Key (Palabra) : Value (Puntaje)

lexico_emocional = {
    # Positivas
    "felicidad": 5,
    "amor": 10,
    "excelente": 8,
    "bueno": 3,
    "genial": 6,
    
    # Negativas
    "triste": -5,
    "odio": -10,
    "error": -8,
    "malo": -3,
    "horrible": -6,
    
    # Neutras (Opcionales, suelen valer 0 o muy poco)
    "normal": 0,
    "quizas": 1
}

usuario_input = input("Escribe algo: ")

texto_limpio = usuario_input.lower()

palabras = texto_limpio.split()

# 1. Creamos el acumulador (La pantalla del precio)
score_total = 0

# 2. El Escáner (Recorremos la lista palabra por palabra)
for palabra in palabras:
    
    # 3. Verificar si la palabra existe en nuestro diccionario
    if palabra in lexico_emocional:
        
        # Si existe, obtenemos su valor
        puntos = lexico_emocional[palabra]
        
        #lo sumamos al total
        score_total += puntos
        
        print(f"encontre '{palabra}' con un puntaje de: {puntos} puntos.")
        
print("-" * 30)
print(f"Resultado Matemático: {score_total}")

if score_total > 0:
    print(">>> Clasificación: 😊 POSITIVO")
    
elif score_total < 0:
    print(">>> Clasificación: 😠 NEGATIVO")
    
else:
    print(">>> Clasificación: 😐 NEUTRO")