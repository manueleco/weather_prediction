import pathlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling
from sklearn.preprocessing import MinMaxScaler

from tensorflow import keras
from tensorflow.keras import layers

#Obtener el dataset
dataset_path='weather_prediction/Final prediction/Otra opcion/weather.csv'
raw_dataset = pd.read_csv(dataset_path, header=0,na_values = "?", comment='\t',sep=",", skipinitialspace=False,parse_dates=[0],index_col=0)
dataset = raw_dataset.copy()

#Separar los datos de entrenamiento con los datos de prueba
train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)

#Relación de variables
sns.pairplot(train_dataset[["temp","hum","presion","altitud"]], diag_kind="kde")
plt.show()

#Estadísticas generales de la data
train_stats = train_dataset.describe()
train_stats.pop("temp")
train_stats = train_stats.transpose()
print(train_stats)

#Separar los labels de la data que queremos predecir
train_labels = train_dataset.pop('temp')
test_labels = test_dataset.pop('temp')

#Normalización
def norm(x):
      return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

#Modelo
def comp_modelo():
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                    optimizer=optimizer,
                    metrics=['mae', 'mse'])
    return model
model = comp_modelo()
model.summary()

#Entrenar al modelo
EPOCHS = 500

#Evitar overfitting
# early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

# early_history = model.fit(normed_train_data, train_labels, 
#                     epochs=EPOCHS, validation_split = 0.2, verbose=0, 
#                     callbacks=[early_stop, tfdocs.modeling.EpochDots()])   


history = model.fit(
  normed_train_data, train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[tfdocs.modeling.EpochDots()])

#Plot del entreno
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch

plt.title("Comportamiento del entreno MAE")
plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)
plotter.plot({'Basic': history}, metric = "mae")
plt.ylim([0, 10])
plt.ylabel('MAE [temp]')
plt.show()

plt.title("Comportamiento del entreno MSE")
plotter.plot({'Basic': history}, metric = "mse")
plt.ylim([0, 20])
plt.ylabel('MSE [temp^2]')
plt.show()

# plotter.plot({'Early Stopping': early_history}, metric = "mae")
# plt.ylim([0, 10])
# plt.ylabel('MAE [temp]')
# plt.show()

loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)
print("Comprobando MAE: {:5.2f} temp".format(mae))


#Predicción
test_predictions = model.predict(normed_test_data).flatten()

#obtener la predicción del siguiente día
results=[]
for i in range(15):
    parcial = model.predict(normed_test_data).flatten()
    results.append(parcial[i])

printRes = [x for x in results]    


predic_v1 = pd.DataFrame(printRes)
predic_v1.plot()
plt.title("Predicción")
plt.xlabel('Horas')
plt.ylabel('Grados C')
plt.show()
predic_v1.to_csv('weather_prediction/Final prediction/Otra opcion/pronostico.csv')

plt.title("Precisión de la predicción")
a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('Valores Reales [test]')
plt.ylabel('Predicciones [test]')
lims = [0, 50]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)
plt.show()

plt.title("Histograma del error de predicción")
error = test_predictions - test_labels
plt.hist(error, bins = 25)
plt.xlabel("Error de predicción [temp]")
_ = plt.ylabel("Cuenta")
plt.show()