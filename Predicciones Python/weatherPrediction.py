#requisitos: python 3, pip 3

#Libreria para extraer la data del CSV
import csv

import math

#Arrays de cada variable medida (temperatura y humedad)
temp = []
hum = []



#temperatura definida para calor
calorTemp = '25'
#temperatura definida para frio
frioTemp = '17'

#humedad agradable para el ser humano
humedadMax = '50'
humedadMin = '30'


#Se carga la data del CSV
with open('weatherData.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        temp.append(row[0])
        hum.append(row[1])


#Ocurrencias de calor
tempOcurrenciesCalor = 0
for i in temp : 
    if i > calorTemp : 
        tempOcurrenciesCalor = tempOcurrenciesCalor + 1

#Ocurrencias de frio
tempOcurrenciesFrio = 0
for i in temp : 
    if i < frioTemp : 
        tempOcurrenciesFrio = tempOcurrenciesFrio + 1

#Ocurrencias de buen tiempo
tempOcurrenciesBueno = 0
for i in temp : 
    if i > frioTemp and i<calorTemp: 
        tempOcurrenciesBueno = tempOcurrenciesBueno + 1

#Ocurrencias de humedad alta
humOcurrenciesMax = 0
for i in hum : 
    if i > humedadMax : 
        humOcurrenciesMax = humOcurrenciesMax + 1

#Ocurrencias de humedad baja
humOcurrenciesMin = 0
for i in hum : 
    if i < humedadMin : 
        humOcurrenciesMin = humOcurrenciesMin + 1

#Ocurrencias de humedad agradable
humOcurrenciesBueno = 0
for i in hum : 
    if i > humedadMin and i < humedadMax: 
        humOcurrenciesBueno = humOcurrenciesBueno + 1

#Cantidad de mediciones de cada variable
cantMedicionesTemp = len(temp)-1
cantMedicionesHum = len(hum)-1

#Probabilidades
probCalor = tempOcurrenciesCalor/cantMedicionesTemp
probFrio = tempOcurrenciesFrio/cantMedicionesTemp

probHumedadAgradable = humOcurrenciesBueno/cantMedicionesHum


#print(temp)
#print(hum)

print("Cantidad de mediciones de temperatura: %2d " %(cantMedicionesTemp))
print("Cantidad de mediciones de humedad: %2d \n" %(cantMedicionesHum))


print("Ocurrencias de Calor: %2d " %(tempOcurrenciesCalor))
print("Ocurrencias de Frio: %2d " %(tempOcurrenciesFrio))
print("Ocurrencias de buen tiempo: %2d \n" %(tempOcurrenciesBueno))

print("Ocurrencias de humedad alta: %2d " %(humOcurrenciesMax))
print("Ocurrencias de humedad baja: %2d " %(humOcurrenciesMin))
print("Ocurrencias de humedad agradable: %2d \n" %(humOcurrenciesBueno))

print("Probabilidad de Calor: %5.2f " %(probCalor))
print("Probabilidad de Frio: %5.2f \n" %(probFrio))

print("Probabilidad de humedad agradable: %5.2f \n" %(probHumedadAgradable))
