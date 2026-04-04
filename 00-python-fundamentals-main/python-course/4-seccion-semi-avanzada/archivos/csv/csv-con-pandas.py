import pandas as pd

#usando la funcion read_csv para leer el archivo csv
data_frame = pd.read_csv("python-course/4-seccion-semi-avanzada/archivos/csv/datos")

#objetiendo datos de la columba nombre
nombres = data_frame["nombre"]

#ordenando el dataframe por la edad
df_ordenado_ascendente = data_frame.sort_values("edad")

#ordenando de forma descendente
df_ordenado_descendente = data_frame.sort_values("edad", ascending=False)

#contatenando 2 data frame
df_concatenado = pd.concat([df_ordenado_ascendente, df_ordenado_descendente])

#accediendo a la primera fila con head()
primera_fila = data_frame.head(1)

#accediendo a la ultima fila con tail
ultima_fila = data_frame.tail(1)

#accediento a la cantidad de filas y columnas con shape
filas_y_columnas = data_frame.shape

#obteniendo data estadistica del dataframe
data_estadistica = data_frame.describe()

#accediento a un elemento especifico del dataframe con loc
elemento_especifico = data_frame.loc[0, "nombre"]

#accediento a un elemento especifico del dataframe con iloc
elemento_especifico_iloc = data_frame.iloc[0, 0]

#accediendo a todas las filas de una columna
apellidos = data_frame.loc[:, "apellido"]

print(data_frame)
