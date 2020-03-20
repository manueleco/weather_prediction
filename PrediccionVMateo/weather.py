import csv
import numpy as np
import random
from operator import lt
   
estados = [] #para poner en array todas las temps del CSV
temp_actual=23.8 #elegir una temperatura para empezar
##poner en estados todos los valores del CSV
with open('weather.csv') as csv_file: #IMPORTANTE: el CSV tiene que estar en la pisma carpeta que el .py y ver que el nombre del CSV en el codigo sea el mismo que el que esta en la carpeta
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
       if line_count == 0:
           line_count += 1
           continue
       else:
           estados.append(float(row[0]))
           line_count += 1
    print(f'Processed {line_count} lines.') #indica cuantos valores se agregaron al array
i=0
transiciones= []# para guerdar cada temperatura con una lista de posibles proximas temperaturas
while i<len(estados):
    if i ==0: #en la primera iteracion solo se guarda el proximo valor xque no hay anterior
        actual1 = estados[0]
        posible = estados[i+1]
        todos=[actual1,[posible]]
        transiciones.append(todos)
    elif i>0: #guardar el valor anterior y siguiente de medida de temperatura actual
        j=0
        actual1 = estados[i]
        while j<len(transiciones):
            if estados[i]==transiciones[j][0]: #comprobar si ya hay entrada para la temperatura que se esta agregando
                existe=1
                pos=j
            j+=1
        if existe: #si existe entrada solo posibles proximas temperaturas a la entrada ya existente
            posible1 = estados[i-1]
            if i+1 ==len(estados):
                break
            posible2 = estados[i+1]
            transiciones[pos][1].append(posible1)
            transiciones[pos][1].append(posible2)
            transiciones[pos][1] = list(dict.fromkeys(transiciones[pos][1])) #limpiar repetidas
            #sorted(transiciones[pos][1])
            transiciones[pos][1].sort() #ordenar de menor a mayor los posibles cambios
            existe=0
            j+=1
        else: #agregar nueva entrada y posibles cambios a transiciones
            j=len(transiciones)
            posible1 = [estados[i-1],estados[i+1]]
            #posible2 = estados[i+1]
            todos=[estados[i],posible1]
            transiciones.append(todos)
            
            j+=1
            
    i+=1
o=0
while o<4: #se va a predecir el clima o veces
    l=0
    for temps in transiciones:
        if temp_actual!=transiciones[l][0]: #buscar temperatura actual en la lista
            l=l+1
        else: #al encontrar la temperatura actual calcular la proxima
            s=0
            x = len(transiciones[l][1])
            x = 1/x #probabilidades para cada cambio te temperatura la suma de todas tiene que ser 1
            #x = x/len(transiciones[l][1])
            probabilidades=[]
            while s<len(transiciones[l][1]):
                probabilidades.append(x) #meter las probabilidades para los cambios en un array
                s=s+1
            new_temp= np.random.choice(transiciones[l][1], 1, replace=True, p=probabilidades)# calcular la proxima temperatura el resultado depende de la distribucion de las probabilidades
            temp_actual=new_temp[0:1][0] #asignar temperatura input para la proxima prediccion
            print("la temperatura en") #imprimir prediccion
            print((o+1)*30)
            print("minutos sera de")
            print(temp_actual)
            print("--------------------------------------------------")
            o=o+1
            break
c=0