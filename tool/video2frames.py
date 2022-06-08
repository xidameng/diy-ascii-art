import cv2
import sys

filename = sys.argv[1]

vidcap = cv2.VideoCapture(str(filename))
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("build/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
