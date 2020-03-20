#requisitos: python 3

#Libreria para extraer la data del CSV
import csv

import math

#Arrays de cada variable medida (temperatura y humedad)
temp = []
hum = []
allData = []



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
        allData.append(row)

#print(allData)

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


#Ocurrencias de calor y humedad alta
calorHumMax = 0
for i in allData : 
    if i[0] > calorTemp and i[1] > humedadMax: 
        calorHumMax = calorHumMax + 1

#Ocurrencias de calor y humedad baja
calorHumMin = 0
for i in allData : 
    if i[0] > calorTemp and i[1] < humedadMin: 
        calorHumMin = calorHumMin + 1

#Ocurrencias de calor y humedad agradable
calorHumBueno = 0
for i in allData : 
    if i[0] > calorTemp and (i[1] < humedadMax and i[1] > humedadMin): 
        calorHumBueno = calorHumBueno + 1

#Ocurrencias de frio y humedad alta
frioHumMax = 0
for i in allData : 
    if i[0] < frioTemp and i[1] > humedadMax: 
        frioHumMax = frioHumMax + 1

#Ocurrencias de frio y humedad baja
frioHumMin = 0
for i in allData : 
    if i[0] < frioTemp and i[1] < humedadMin: 
        frioHumMin = frioHumMin + 1

#Ocurrencias de frio y humedad agradable
frioHumBueno = 0
for i in allData : 
    if i[0] < frioTemp and (i[1] < humedadMax and i[1] > humedadMin): 
        frioHumBueno = frioHumBueno + 1


#Ocurrencias de temperatura agradable y humedad alta
buenClimaHumMax = 0
for i in allData : 
    if (i[0] > frioTemp and i[0] < calorTemp)  and i[1] > humedadMax: 
        buenClimaHumMax = buenClimaHumMax + 1

#Ocurrencias de temperatura agradable y humedad alta
buenClimaHumMin = 0
for i in allData : 
    if (i[0] > frioTemp and i[0] < calorTemp) and i[1] < humedadMin: 
        buenClimaHumMin = buenClimaHumMin + 1

#Ocurrencias de temperatura agradable y humedad alta
buenClimaHumBueno = 0
for i in allData : 
    if (i[0] > frioTemp and i[0] < calorTemp) and (i[1] < humedadMax and i[1] > humedadMin): 
        buenClimaHumBueno = buenClimaHumBueno + 1

#Cantidad de mediciones de cada variable
cantMedicionesTemp = len(temp)-1
cantMedicionesHum = len(hum)-1

#Probabilidades
probCalor = tempOcurrenciesCalor/cantMedicionesTemp
probFrio = tempOcurrenciesFrio/cantMedicionesTemp

probHumedadAgradable = humOcurrenciesBueno/cantMedicionesHum


#print(temp)
#print(hum)

print("\nCantidad de mediciones de temperatura: %2d " %(cantMedicionesTemp))
print("Cantidad de mediciones de humedad: %2d \n" %(cantMedicionesHum))


print("Ocurrencias de Calor: %2d " %(tempOcurrenciesCalor))
print("Ocurrencias de Frio: %2d " %(tempOcurrenciesFrio))
print("Ocurrencias de buen tiempo: %2d \n" %(tempOcurrenciesBueno))

print("Ocurrencias de humedad alta: %2d " %(humOcurrenciesMax))
print("Ocurrencias de humedad baja: %2d " %(humOcurrenciesMin))
print("Ocurrencias de humedad agradable: %2d \n" %(humOcurrenciesBueno))

print("Ocurrencias de calor y humedad alta: %2d " %(calorHumMax))
print("Ocurrencias de calor y humedad baja: %2d " %(calorHumMin))
print("Ocurrencias de calor y humedad agradable: %2d \n" %(calorHumBueno))

print("Ocurrencias de frio y humedad alta: %2d " %(frioHumMax))
print("Ocurrencias de frio y humedad baja: %2d " %(frioHumMin))
print("Ocurrencias de frio y humedad agradable: %2d \n" %(frioHumBueno))

print("Ocurrencias de temperatura agradable y humedad alta: %2d " %(buenClimaHumMax))
print("Ocurrencias de temperatura agradable y humedad baja: %2d " %(buenClimaHumMin))
print("Ocurrencias de temperatura agradable y humedad agradable: %2d \n" %(buenClimaHumBueno))

print("Probabilidad de Calor: %5.2f " %(probCalor))
print("Probabilidad de Frio: %5.2f \n" %(probFrio))

print("Probabilidad de humedad agradable: %5.2f \n" %(probHumedadAgradable))
