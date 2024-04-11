import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.callbacks import LearningRateScheduler
from keras.callbacks import History
from keras.callbacks import EarlyStopping
from keras.callbacks import TensorBoard
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization, Convolution2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.optimizers import RMSprop
from keras import losses

#get params
param = snakemake.output["model"]


#Load train data
X_train = np.load(snakemake.input["X_train"])
X_val = np.load(snakemake.input["X_val"])

y_train = pd.read_csv(snakemake.input["y_train"])
y_train = y_train.drop(columns=['Unnamed: 0'])

y_val = pd.read_csv(snakemake.input["y_val"])
y_val = y_val.drop(columns=['Unnamed: 0'])

#set image params
height = 50
width = 50
channel = 3

#reshaping samples according to sample size
X_train = X_train.reshape(-1,width,height, channel)
X_val = X_val.reshape(-1,width,height, channel)

#define hyperparameters
epochs = int(param.split("_")[2])
batch_size = int(param.split("_")[3])

# construct model
model = Sequential()

# Layers
model.add(Convolution2D(32,
                 kernel_size=(3,3),
                 activation='relu',
                 input_shape=(width,
                              height,
                              channel)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(64,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(128,kernel_size=(3,3),activation='relu'))
model.add(Dropout(0.25))
model.add(Flatten())

model.add(Dense(298, activation="relu"))
model.add(Dense(149,activation="softmax"))

# compiling
model.compile(optimizer=param.split("_")[1], 
              loss="categorical_crossentropy", 
              metrics=["accuracy"])


model.summary()


#train
model_history = model.fit(X_train, y_train,
                  epochs=epochs,
                  batch_size=batch_size,
                  verbose = 1,
                  validation_data = (X_val, y_val),
                  callbacks=[EarlyStopping(monitor='val_loss', patience=5)])



# save history
print("saving history...")
hist_df = pd.DataFrame(model_history.history) 
hist_df.to_csv(snakemake.output["history"])

#save model
print("saving model...")
model.save(snakemake.output["model"])


# Plot the accuracy
plt.figure(figsize=(8,5))
plt.title('Accuracy')
plt.plot(np.sqrt(model_history.history['accuracy']), 'r', label='train')
plt.plot(np.sqrt(model_history.history['val_accuracy']), 'b' ,label='val')
plt.xlabel('epochs', fontsize=15)
plt.ylabel('Accuracy', fontsize=15)
plt.legend()
plt.savefig(snakemake.output["eval"])

         
# Plot the loss function
plt.figure(figsize=(8,5))
plt.title('Loss funtion')
plt.plot(np.sqrt(model_history.history['loss']), 'r', label='train')
plt.plot(np.sqrt(model_history.history['val_loss']), 'b' ,label='val')
plt.xlabel('epochs', fontsize=15)
plt.ylabel('loss', fontsize=15)
plt.legend()
plt.savefig(snakemake.output["loss"])

