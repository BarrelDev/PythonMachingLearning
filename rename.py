from os import rename
from os import walk

path = "D:\\Python\\hand maching\\handPos5Gray"
print("bvoib")
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
print("bvoib")
z=0

for s in f:
    rename(path+"\\"+s, path+"\\4_"+str(z)+".png")
    z+=1

