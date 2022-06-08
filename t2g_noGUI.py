import numpy as np
from PIL import Image
import sys

print("This program takes in 2 arguments, 1st is the image file(string), 2nd is the character pattern(a string in the order from loose to dense, seperated by ; ")

txtname = ''
imagefile = ''
charPattern = ''

imagefile = sys.argv[1]
charPattern = sys.argv[2]
print(imagefile)
print(charPattern)
str = charPattern.split(";")
print(str)
txtname = imagefile+'.txt'



im = Image.open(imagefile)
im = im.resize((150, 150), Image.ANTIALIAS)
#im = im.resize((300, 300), Image.ANTIALIAS)
image = im.convert('L')
image = np.array(image)
if len(str) == 3:
    with open(txtname, 'w') as f:
        for i in range(len(image)):
            for j in range(len(image[0])):
                st = int(image[i][j] / 85)
                if st == 0:
                    f.write(str[0])
                else:
                    if st == 1:
                        f.write(str[1])
                    else:
                        f.write(str[2])
                f.write(" ")
            f.write("\n")
elif len(str) == 2:
    with open(txtname, 'w') as f:
        for i in range(int(len(image))):
            for j in range(int(len(image[0]))):
                if image[i][j] > 95:
                    f.write(str[0])
                else:
                    f.write(str[1])
                # f.write(str(abs(int((255 - binary[int(i)][int(j)])/255)-1)))
            f.write("\n")
else:
    print("Only support 2 char / 3 char pattern now! ")

