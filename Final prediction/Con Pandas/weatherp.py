import numpy as np 
from datetime import datetime, timedelta
import time
from collections import namedtuple
import pandas as pd
import requests
import matplotlib.pyplot as plt
from IPython.display import display



weatherLike = pd.read_csv("weather.csv")
#para comprobar que se estén jalando los datos
#print(weatherLike)

df1 = pd.DataFrame(weatherLike, columns=['dia','hora','temtemp_DHT','hum_DHT','temp_BMP','presion_BMP','altitud_BMP'])
print(df1)

#codigo para jalar info en general
#tempMax = df1.groupby(['dia'])['temtemp_DHT'].max()
#tempMin = df1.groupby(['dia'])['temtemp_DHT'].min()
#meanHumPress = df1.groupby(['dia'])['hum_DHT','presion_BMP'].mean()

#agregacion para escoger parametros de las columnas
aggregacion = {"temtemp_DHT":['max', 'min'], 
              "hum_DHT":['mean'], 
              "presion_BMP":['mean'],  
              }

allData = df1.groupby(['dia']).agg(aggregacion)

#mirar las columnas que voy a usar
#print("soy data columns",allData.columns)

#print(tempMax)
#print(meanHumPress)

print(allData)



type(weatherLike)

len(weatherLike)

weatherLike.shape

weatherLike.head()
pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)
weatherLike.tail()
#print(weatherLike.tail())