import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar los datos (Los jugadores en la cancha, animales en este caso )
data_frame = pd.read_csv("04-knn-visual/datos.csv")

print("--- DETECTOR DE ANIMALES ---")
nuevo_peso = float(input("Ingresa el peso del animal (kg): "))
nueva_altura = float(input("Ingresa la altura del animal (cm): "))

# CALCULAR DISTANCIAS -------------------------------------
distancias = []

for indice, fila in data_frame.iterrows():
    peso_actual = fila["peso"]
    altura_actual = fila["altura"]
    tipo_animal = fila["animal"]
    
    # Distancia = RaízCuadrada( DiferenciaPeso² + DiferenciaAltura² )

   # 2. Pitágoras (Distancia Euclidiana)
    diferencia_peso = peso_actual - nuevo_peso
    diferencia_altura = altura_actual - nueva_altura
    
    # La fórmula: Raíz de (a² + b²)
    distancia = math.sqrt(diferencia_peso ** 2 + diferencia_altura ** 2)
    
    # 3. Guardamos el resultado: (Distancia, Qué animal es)
    distancias.append({"animal": tipo_animal, "distancia": distancia})

print("-" * 30)
print("Distancias calculadas:")
for d in distancias:
    
    # Imprimimos: Animal y su distancia (redondeada a 2 decimales)
    print(f"-> {d['animal']}: {d['distancia']:.2f}")
    print("-" * 30)


# 2. Preparar el lienzo
plt.figure(figsize=(8, 6))

plt.title("Mapa de Mascotas: Peso vs Altura ( + El Misterio )")

# 3. Dibujar los puntos
sns.scatterplot(data=data_frame, x="peso", y="altura", hue="animal", s=100)
plt.scatter(nuevo_peso, nueva_altura, color='red', marker='X', s=200, label='Misterio')
plt.legend()


# 4. Mostar
plt.grid(True, alpha=0.3)
plt.show()


# 1. ordenar la lista de menor distancia a mayor
# "ordenar la lista 'distancias', usando como clave el valor de 'distancia'"
distancias.sort(key=lambda x: x["distancia"])

k = 3
vecinos_cercanos = distancias[:k] # k vecinos mas cercanos

print("\n" + "-" * 30)
print(f"--- RESULTADO: LOS {k} VECINOS MÁS CERCANOS ---")

conteo_gatos = 0
conteo_perros = 0

for vecino in vecinos_cercanos:
    animal = vecino["animal"]
    dist = vecino["distancia"]
    
    print(f"Vecino encontrado: {animal} a una distancia de {dist:.2f}")
    
    # conteo de votos
    if animal == "gato":
        conteo_gatos += 1
    elif animal == "perro":
        conteo_perros += 1

print("-" * 30)

if conteo_gatos > conteo_perros:
    print(f">>> CLASIFICACIÓN: ES UN GATO 🐱 ({conteo_gatos} vs {conteo_perros})")
else:
    print(f">>> CLASIFICACIÓN: ES UN PERRO 🐶 ({conteo_perros} vs {conteo_gatos})")