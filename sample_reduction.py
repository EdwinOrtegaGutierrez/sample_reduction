import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
data, dataNorm  = pd.read_csv("Datos_semana_02.csv", encoding='latin1'), pd.read_csv("datos_normalizados.csv", encoding='latin1')

# Normalizar datos
def normalized_data(data):
    # filter data
    data = data[["Estatura", "Peso", "Altura"]] 
    data_norm = (data - data.mean(numeric_only=True)) / data.std(numeric_only=True)
    return data_norm

def dist_euclidian(data):
    # Extraer las columnas relevantes del dataframe
    data_cols = data[["Estatura", "Peso", "Altura"]]

    # Convertir las columnas del dataframe en una matriz NumPy
    data_mat = data_cols.to_numpy()

    # Calcular las distancias euclidianas entre cada par de puntos
    dist = np.sqrt(np.sum((data_mat[:, np.newaxis, :] - data_mat[np.newaxis, :, :]) ** 2, axis=-1))

    return dist, data_mat

def delete_Neighbor(data):
    # Calcular la matriz de distancias euclidianas
    dist, data_mat = dist_euclidian(data)

    # Encontrar el índice del punto con la distancia euclidiana más corta
    min_index = np.unravel_index(np.argmin(dist), dist.shape)

    # Eliminar la fila y columna correspondientes al punto con la distancia euclidiana más corta
    data_mat = np.delete(data_mat, min_index[0], axis=0)
    data_mat = np.delete(data_mat, min_index[1], axis=1)

    return data_mat

# Guardar datos normalizados en un archivo csv
def save_data(data): data.to_csv("datos_normalizados.csv", index=False)

# Graficar 
def grafic(matriz):
    # aplanar la matriz y crear un arreglo para las posiciones en "x" y "y"
    x, y = np.ravel(matriz), np.arange(len(np.ravel(matriz)))

    # graficar la nube de puntos
    plt.scatter(x, y)

    # mostrar el gráfico
    plt.show()

grafic(delete_Neighbor(dataNorm))