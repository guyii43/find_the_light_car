import cv2
import numpy as np
import numpy
import time

##shink the image
img = cv2.imread("g:/samples/test9.jpg")
size = (372,496)        #set the height and width
#size = (96,128)
shrink = cv2.resize(img,size,cv2.INTER_AREA)
cv2.namedWindow("shrink",0)
cv2.imshow("shrink",shrink)
cv2.waitKey()
cv2.imwrite("g:/samples/shrink5.jpg",shrink)


blacklower = np.array([0,0,9])
blackupper = np.array([180,255,46])
hsv = cv2.cvtColor(shrink,cv2.COLOR_BGR2HSV)
blackmask = cv2.inRange(hsv,blacklower,blackupper)

cv2.namedWindow("blackmask",0)
cv2.imshow("blackmask",blackmask)
cv2.waitKey()