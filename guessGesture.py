import numpy as np
import cv2 as cv
from PIL import Image, ImageFilter
from keras.models import Sequential
from tkinter import *
import tensorflow as tf
from tensorflow import keras

def guess():
    guessLabel = Label(frame, text = "")
    guessLabel.pack()
    vdo = cv.VideoCapture(0+cv.CAP_DSHOW)
    retval,userImg = vdo.read()
    vdo.release()
    # Destroy all the windows
    cv.destroyAllWindows()
    if retval != True:
        print("Can't read frame")
        guessLabel = Label(frame, text = "cant read")
        guessLabel.pack()
        return 5
    userImg = cv.cvtColor(userImg, cv.COLOR_BGR2GRAY)
    userImg = cv.resize(userImg, (48, 36), interpolation = cv.INTER_CUBIC)
    cv.imshow('frame',userImg)

    np_img = np.asarray(userImg)
    np_img = np.delete(np_img, 2, 2)
    np_img = np.delete(np_img, 1, 2)
    np_img = np.reshape(np_img, (36, 48, 1))

    model = keras.models.load_model(os.getcwd() + '\\test-model-epoch5.h5')
    probability_model = Sequential([model, tf.keras.layers.Softmax()])
    predictions = probability_model.predict(np_img)
    np.argmax(predictions[0])
    if predictions[0]==0:
        guessLabel = Label(frame, text = "Palm(Vertical)")
    elif predictions[0]==1:
        guessLabel = Label(frame, text = "Palm(Horizontal)")
    elif predictions[0]==2:
        guessLabel = Label(frame, text = "1 finger")
    elif predictions[0]==3:
        guessLabel = Label(frame, text = "Fist")
    elif predictions[0]==4:
        guessLabel = Label(frame, text = "Thumbs Up")
    guessLabel.pack()


root = Tk()
root.geometry("640x480")
frame = Frame(root)
frame.pack()
label = Label(frame, text = "Click to Guess your Hand Gesture!")
label.pack()

testButton = Button(frame, text = "Guess", command = guess)
testButton.pack(padx = 3, pady = 3)

root.title("Guess Gesture")
root.mainloop()
