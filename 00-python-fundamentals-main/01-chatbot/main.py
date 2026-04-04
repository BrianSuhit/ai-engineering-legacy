# 1- definir variables
nombre_bot = "Yor"

# 2- saludar
print(f"Hola soy {nombre_bot}, la asistente virtual de Brian y estoy aquí para ayudarte. Escribe 'salir' para terminar")
print("-" * 30) # Esto hace una línea separadora visual

# 3- bucle infinito ( el programa vive aca dentro )
while True:
    usuario_input = input("Vos: ") # 4- escuchar al usuario ( input )
    
    texto_limpio = usuario_input.lower() # 5. Normalizar texto (todo a minúsculas para comparar fácil)
    
    # --- CEREBRO DEL BOT ---

    # 6. Lógica de salida
    if texto_limpio == "salir":
        print(f"{nombre_bot}: ¡Un gusto hablar con vos! Adiós.")
        break # <--- ESTO ROMPE EL BUCLE Y TERMINA EL PROGRAMA
    
    elif "experiencia" in texto_limpio:
        print(f"{nombre_bot}: Brian es estudiante de TUDAI (tecnicatura universitaria en desarrollo de apliaciones informaticoas) en UNICEN. Su especializad es Ai Engineering.")
        
    elif "proyectos" in texto_limpio or "proyecto" in texto_limpio or "portfolio" in texto_limpio:
        print(f"{nombre_bot}: ¡Tiene un portfolio web desplegado en Netlify y proyectos de código en GitHub!. Este es el link al mismo: https://briansuhit-portfolio.netlify.app/")
        
    elif "contacto" in texto_limpio or "email" in texto_limpio:
        print(f"{nombre_bot}: Puedes escribirle a braisuhit@gmail.com")
        
    else:
        print(f"{nombre_bot}: Mmm, no entendí eso. Intenta preguntar por 'experiencia' o 'contacto'.")
