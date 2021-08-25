from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from os import walk
import pandas as pd
from sklearn.model_selection import train_test_split

mypath = "D:/Python/hand maching/AllSamples/"
x = []
y = []

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
  for fl in filenames:
    if '.png' in fl:
      f.append(fl)


for i in f:
    folderlabel = int(i.split('_')[0])
    img = Image.open("D:/Python/hand maching/AllSamples/"+ i)
    np_img = np.asarray(img)
    np_img2 = np.delete(np_img, 2, 2)
    np_img2 = np.delete(np_img2, 1, 2)
    np_img2 = np_img2.reshape(1728)
    x.append(np_img2)
    y.append(folderlabel)
x = np.array(x, dtype="uint8", )
x = np.reshape(x, (len(f), 36, 48, 1))

print(x.ndim)
y = np.array(y)

ts = 30
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=ts, random_state=46)
x_train,x_val, y_train, y_val = train_test_split(x_train,y_train, test_size=ts, random_state=46)

from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten

featureLength = len(x_train[0])
print(featureLength)
# Construction of model
model = Sequential()
model.add(Conv2D(32, (5, 5), activation='relu', input_shape=(36,48,1))) 
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu')) 
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', # Optimization routine, which tells the computer how to adjust the parameter values to minimize the loss function.
              loss='sparse_categorical_crossentropy', # Loss function, which tells us how bad our predictions are.
              metrics=['accuracy']) # List of metrics to be evaluated by the model during training and testing.
model.fit(x_train, y_train, epochs=5, batch_size=64, verbose=2, validation_data=(x_val, y_val))

