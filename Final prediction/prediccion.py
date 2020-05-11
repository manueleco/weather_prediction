import numpy as np    # Pandas está basado en NumPy (Numerical Python) por lo que hay que importarlo también
import pandas as pd
import requests       #  Módulo con funciones para obtener archivos desde la Internet

# Pandas tiene su módulo para hacer gráficas basado en otro módulo
#    llamado MatPlotLib, se usa esta instrucción para que las gráficas salgan en Notebook
#%matplotlib inline    
url_datos_fuente = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
path_en_mi_compu = "nba_all_elo.csv"
respuesta = requests.get(url_datos_fuente)
respuesta.raise_for_status()
with open(path_en_mi_compu, "wb") as f:
    f.write(respuesta.content)
print("Descarga, lista!")
nba = pd.read_csv("nba_all_elo.csv")

type(nba)
len(nba)
nba.shape
nba.head()
pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)
nba.tail()
print(nba.tail())