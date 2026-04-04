import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("python-course/4-seccion-semi-avanzada/archivos/graficos/entrenamiento_ia.csv")


print(data_frame.head()) # Para ver si cargó

plt.figure(figsize=(10, 6))

# El gráfico mágico de Seaborn
sns.lineplot(data=data_frame, x="epoca", y="precision", hue="modelo", marker="o")

# Mostrar
plt.show()