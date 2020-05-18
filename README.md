# Predicción de clima en el área de Zona 15, Ciudad de Guatemala
Proyecto de medición de variables climáticas para predecir el clima para la clase de Inteligencia Artificial.


## Distribución del Repo
* **/arduino** _Código de arduino_
  * Templates
  * Código utilizado en el arduino Mega 2560
* **/Prediction** _Código de python para las predicciones_
  * **/prediction.py** programa de Python para determinar las próximas temperaturas a través de distribución de frecuencias y cadenas de Markov
* **/Final Prediction** _Código de python para las predicciones utilizando redes neuronales_
  * **/prediction.py** 
  * **/Otra Opcion/PredFinal.py** Script para predecir la temperatura en base al registro obtenido con los sensores.
* **/'Bayes for weather'** _Código de Python aplicando teorema de Bayes_ 
  * **/weatherPredictionBayes.py** programa de Python para determinar probabilidades con el teorema de Bayes
  

### Arduino para las mediciones
 
 Para las mediciones del arduino se utilizaron los siguientes componentes:
 * Arduino Mega 2560
 * Sensor DHT11
 * Sensor BMP280
 
 
### Preparación de los datos
En caso que exista un error en **/Otra Opcion/PredFinal.py** hay que verificar lo siguiente:
* Que los datos numéricos tengan 2 números decimales (para ser tomados como float)
* Verificar el formato de las fechas en el .csv dentro de la carpeta
* **Observación:** Sobre los datos iniciales obtenidos con los sensores, se realizó un promedio entre las dos medidas de temperatura obtenidas, para solo tener una columna con los datos de la temperatura. 


