from PIL import Image, ImageFilter
from os import walk

mypath = "C:\\Users\\visva\\Desktop\\hand maching\\handPos5"

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)


for i in f:
    image = Image.open("C:\\Users\\visva\\Desktop\\hand maching\\handPos5\\"+ i)
    gray = image.convert('L')
    imageQuality = 5
    gray.save(i, quality = int(imageQuality))