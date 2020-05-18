import numpy as np
import matplotlib
from datetime import datetime, timedelta
import time
from collections import namedtuple
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, median_absolute_error


weatherLike = pd.read_csv("weather.csv")
# para comprobar que se estén jalando los datos
# print(weatherLike)

df1 = pd.DataFrame(weatherLike, columns=[
                   'dia', 'hora', 'temtemp_DHT', 'hum_DHT', 'temp_BMP', 'presion_BMP', 'altitud_BMP'])

print('========== INFO ===========')
print(df1)

# codigo para jalar info en general
#tempMax = df1.groupby(['dia'])['temtemp_DHT'].max()
#tempMin = df1.groupby(['dia'])['temtemp_DHT'].min()
#meanHumPress = df1.groupby(['dia'])['hum_DHT','presion_BMP'].mean()

# agregacion para escoger parametros de las columnas
aggregacion = {"temtemp_DHT": ['max', 'min', 'mean'],
               "hum_DHT": ['max', 'min', 'mean'],
               "presion_BMP": ['max', 'min', 'mean'],
               }

allData = df1.groupby(['hora']).agg(aggregacion)

allData.columns = ["_".join(x) for x in allData.columns.ravel()]

dataClean = allData.sort_values('hora', ascending=True)

print('========== FORMATO DE INFO ===========')
dataClean.info()

# mirar las columnas que voy a usar
#print("soy data columns",allData.columns)

print('========== DATA ARREGLADA, LISTA PARA USAR ===========')
print(dataClean)

# ======================================= PARA DEPURAR LA INFORMACIóN ====================
"""
#Ver la dispersion de la informacion
dispersion = df1.describe().T

#Para precalcular los interquartiles donde se encuentra la info
IQR = dispersion['75%'] - dispersion['25%']
dispersion['atipicos'] = (dispersion['min']<(dispersion['25%']-(3*IQR)))|(dispersion['max'] > (dispersion['75%']+3*IQR))
spreadness = dispersion.iloc[dispersion.atipicos,]

print(spreadness)
"""

plt.rcParams['figure.figsize'] = [14, 8]
plt.rcParams['figure.figsize'] = [14, 8]
dataClean.temtemp_DHT_max.hist()
plt.title('Distribucion de temperatura max')
plt.xlabel('temtemp_DHT_max')
"""
dataClean.presion_BMP_mean.hist()
plt.title('Distribution of presion_BMP_mean')
plt.xlabel('presion_BMP_mean')
"""
# plt.show()

# ======================================= CORRELACIONES ====================
print('========== CORRELACIONES ===========')

# determinar correlacion entre temperatura media
dataCorrelation = dataClean.corr(
)[['temtemp_DHT_mean']].sort_values('temtemp_DHT_mean')
print(dataCorrelation)

predictores = ['temtemp_DHT_max',
               'temtemp_DHT_min',
              
               'presion_BMP_max',
               'presion_BMP_min',
               'presion_BMP_mean']

df2 = dataClean[['temtemp_DHT_mean']+predictores]

print(df2)
#print('======== los predictores =========')
#print(predictores)

# ======================================= VISUALZACION DE CORRELACIONES ====================

#ajusta columnas y filas de acuerdo a la cantidad de info a display
plt.rcParams['figure.figsize'] = [10, 10]
fig, axes = plt.subplots(nrows=5, ncols=2)
arr = np.array(predictores).reshape(5,1)


for row, col_arr in enumerate(arr):
    for col, feature in enumerate(col_arr):
        axes[row, col].scatter(df2[feature], df2['temtemp_DHT_mean'])
        if col == 0:
            axes[row, col].set(xlabel=feature, ylabel='temtemp_DHT_mean')
        else:
            axes[row, col].set(xlabel=feature)
#plt.show()


matplotlib.style.use('ggplot')

print(df2['temtemp_DHT_max'])
print(df2['temtemp_DHT_mean'])


plt.scatter(df2['temtemp_DHT_max'], df2['temtemp_DHT_mean'])
#plt.show()

# ====================== BACKWARD ELIMINATION ===============
xx = df2[predictores]
y231 = df2['temtemp_DHT_mean']

#xx = sm.add_constant(xx)
xx = xx.drop(['presion_BMP_min','presion_BMP_mean','presion_BMP_max'], axis=1)

x11 = sm.add_constant(xx)

XX = x11.iloc[:96,:96]
print('========== backward elimination ===========')
print(XX)


alpha = 0.05

model = sm.OLS(y231, XX).fit()

lemodel = model.summary()
print(lemodel)

# ==================== REGRESIONES LINEALES PARA PREDECIR
print(XX)
X = XX.drop('const', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y231, test_size=0.3, random_state=12)

#X_train = X_train.values.reshape(-1, 1)
#y_train = y_train.values.reshape(-1, 1)

regressor = LinearRegression()

miRegresion = regressor.fit(X_train, y_train)

# ==========  PRE PREDICCION 
prediction = regressor.predict(X_test)
print("Varianza: %.2f" % regressor.score(X_test, y_test))

print("MeanAE: %.2f celsius" % mean_absolute_error(y_test, prediction))
print("MedianAE: %.2f celsius" % median_absolute_error(y_test, prediction))
