# Reading an animated GIF file using Python Image Processing Library - Pillow

from PIL import Image
from PIL import GifImagePlugin
import sys

filename = sys.argv[1]
imageObject = Image.open(str(filename))
print(imageObject.is_animated)
print(imageObject.n_frames)

 

# Display individual frames from the loaded animated GIF file

for frame in range(0,imageObject.n_frames):
    imageObject.seek(frame)
    imageObject.show()
    imageObject.save("build/gif_frame"+str(frame)+".png")
