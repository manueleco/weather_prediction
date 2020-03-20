import csv
import math
import numpy as np

rangeSize = 6

#obtener las marcas de clase y las frecuencias del array deseado
def getInfo(lista):
    valNum = len(lista)
    maximo = max(lista)
    minimo = min(lista)
    ancho = maximo-minimo
    intervalo = ancho/rangeSize
    classMark = []
    j = 0

    checkingValue = minimo - intervalo
    while (j<=rangeSize+1):
        checkingValue = checkingValue + intervalo
        classMark.insert(j,round(checkingValue,2))
        j += 1

    freq = []
    k = 0
    while k < rangeSize+1:
        suma = 0
        for num in lista:
            if (classMark[k]<=num<classMark[k+1]):
                suma += 1
            else:
                pass
        freq.insert(k,suma)
        k+=1
    answ = [classMark,freq]
    return answ

#Realiza la suma de las frecuencias
def sumFreq(lista):
    suma = 0
    for item in lista:
        suma = suma + item
    return suma

#Obtiene la probabilidad de cada marca de clase
def getProb(listaF,total):
    prob = []
    k = 0
    for item in listaF:
        prob.insert(k,item/total)
        k+=1
    return prob

#Imprimir probabilidades
def imprimir(marcas,freq,prob,tag):
    print('################### {} ###################'.format(tag))
    print("Marcas de clase \t Frecuencias \t Probabilidad")
    k = 0
    limite = len(freq)
    for item in range(0,limite):
        
        print('{:0.2f} - {:0.2f} \t\t {} \t\t {:0.2f} '.format(marcas[k],marcas[k+1],freq[k],prob[k]))
        #print(f'Column names are {", ".join(row)}')
        k+=1
    print('\n')     

#Funcion de predicción en base a probabilidades
#Saca el indice del rango de la posible probabilidad
def getNext(freq,probabilidades):
    indices = []
    for item in range(0,len(freq)):
        indices.insert(item,item)
    nuevo = np.random.choice(indices, 1, replace=True, p=probabilidades)# calcular la proxima temperatura el resultado depende de la distribucion de las probabilidades
    actual=nuevo[0:1][0] #asignar temperatura input para la proxima prediccion
    return actual

#Obtener las temperaturas y la humedad desde el archivo csv
temps = []
humids = []
with open('weather_prediction/Prediction/temps2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} , {row[1]}.')
            temp = float(row[0])
            temps.insert(i,temp)
            temp = float(row[1])
            humids.insert(i,temp)
            line_count += 1
            i+=1


#Marcas de clase, frecuencia y probabilidad de la temperatura
infoTemp = getInfo(temps)
markTemp = infoTemp[0]
freqTemp = infoTemp[1]
probTemp = getProb(freqTemp,sumFreq(freqTemp))

#Marcas de clase, frecuencia y probabilidad de la humedad
infoHum = getInfo(humids)           #Este solo es para obtener el array de las marcas y las frecuencias para luego separarlo
markHum = infoHum[0]
freqHum = infoHum[1]
probHum = getProb(freqHum,sumFreq(freqHum))

#Imprimir tabla de probabilidades
imprimir(markTemp,freqTemp,probTemp,' Temperatura ')
imprimir(markHum,freqHum,probHum,' Humedad ')

#Predecir las 5 siguientes temperaturas y humedades
k = 0
while k<7:
    k +=1
    tiempo = (k*30)
    #Temperatura
    resultadoTemp = getNext(freqTemp,probTemp)
    resultadoHum = getNext(freqHum,probHum)
    print('En {} min la temperatura será de: {:0.2f} - {:0.2f} y la humedad: {:0.2f}% - {:0.2f}%'.format(tiempo,markTemp[resultadoTemp],markTemp[resultadoTemp+1],markHum[resultadoHum],markHum[resultadoHum+1]))