import cv2
from os import walk

mypath = "C:\\Users\\visva\\Desktop\\hand maching\\handPos5Gray"

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)


for i in f:
    image = cv2.imread("C:\\Users\\visva\\Desktop\\hand maching\\handPos5Gray\\"+ i)
    resize = cv2.resize(image, (48, 36), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite("C:\\Users\\visva\\Desktop\\hand maching\\handPos5Gray\\"+ i, resize)
    