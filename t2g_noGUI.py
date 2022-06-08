import numpy as np
from PIL import Image
import sys

print("## This program takes in 3 arguments")
print("- 1st is the image file(string)")
print("- 2nd is the character pattern(a string in the order from loose to dense)")
print("  Please seperate them using ';' ")
print("- 3rd is the resolution(default at 300p)")

txtname = ''
imagefile = ''
charPattern = ''

imagefile = sys.argv[1]
charPattern = sys.argv[2]
resolution = int(sys.argv[3])
print(imagefile)
print(charPattern)
str = charPattern.split(";")
print(str)
txtname = imagefile.split('/')[-1]
txtname = txtname.split('.')[0]+'.txt'
print(txtname)



im = Image.open(imagefile)
im = im.resize((resolution, resolution), Image.ANTIALIAS)
#im = im.resize((resolution, resolution), Image.ANTIALIAS)
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

print("job done")
