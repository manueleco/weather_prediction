import pathlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

from tensorflow import keras
from tensorflow.keras import layers

#Obtener el dataset
dataset_path='weather_prediction/Final prediction/Otra opcion/weather.csv'
#column_names = ["timestamp","temp","hum","presion","altitud"]
raw_dataset = pd.read_csv(dataset_path, header=0,na_values = "?", comment='\t',sep=",", skipinitialspace=False,parse_dates=[0],index_col=0)
#dataset = pd.read_csv('weather_prediction/Final prediction/Otra opcion/weather.csv',  parse_dates=[0], header=0,index_col=0, squeeze=True)
dataset = raw_dataset.copy()

#Separar los datos de entrenamiento con los datos de prueba
train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)

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
EPOCHS = 1000

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
#print(hist.tail())

plotter = tfdocs.plots.HistoryPlotter(smoothing_std=2)
plotter.plot({'Basic': history}, metric = "mae")
plt.ylim([0, 10])
plt.ylabel('MAE [temp]')
plt.show()

plotter.plot({'Basic': history}, metric = "mse")
plt.ylim([0, 20])
plt.ylabel('MSE [temp^2]')
plt.show()

# plotter.plot({'Early Stopping': early_history}, metric = "mae")
# plt.ylim([0, 10])
# plt.ylabel('MAE [temp]')
# plt.show()

