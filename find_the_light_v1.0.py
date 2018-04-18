#-*-coding:utf-8-*-
#code by yyt
#version1.0
    # 1.?????????
    # 2.shrink the image
    # 3.pick the red block
    # 4.pick the blakc blokc
    # 5.get the centre of the block





import cv2
import numpy as np
import numpy
import time

##################################shink the image########################################
img = cv2.imread("g:/samples/test11.jpg")
size = (372,496)        #set the height and width
print(type(img))
print(img.shape)
shrink = cv2.resize(img,size,cv2.INTER_AREA)
cv2.namedWindow("shrink",0)
cv2.imshow("shrink",shrink)
cv2.waitKey()
cv2.imwrite("g:/samples/shrink5.jpg",shrink)


start = time.clock()
###################################pick the red block#####################################
redlower = np.array([150,80,80])
redupper = np.array([179,255,255])
hsv = cv2.cvtColor(shrink,cv2.COLOR_BGR2HSV )
redmask = cv2.inRange(hsv,redlower,redupper)


# cv2.namedWindow("pick_red",0)
# cv2.imshow("pick_red",redmask)
# cv2.waitKey()
# print(redmask.shape)


###################################pick the black block#######################################
blacklower = np.array([0,0,9])
blackupper = np.array([180,255,46])
blackmask = cv2.inRange(hsv,blacklower,blackupper)

# cv2.namedWindow("pick_black",0)
# cv2.imshow("pick_black",blackmask)
# cv2.waitKey()

####################################make the binary image#############################
# cv2.imwrite("g:/samples/redmask5.jpg",redmask)
ret,redbinary = cv2.threshold(redmask,120,255,cv2.THRESH_BINARY)

# cv2.namedWindow("redbinary",0)
# cv2.imshow("redbinary",redbinary)
# cv2.waitKey()
# cv2.imwrite("g:/samples/redbinary5.jpg",redbinary)
# print(redbinary.shape)

#pick the white block
# whitelower = np.array([0,0,175])
# whiteupper = np.array([100,40,240])
# whitemask = cv2.inRange(hsv,whitelower,whiteupper)
# cv2.namedWindow("jj2",0)
# cv2.imshow("jj2",whitemask)
# cv2.waitKey()

mymoment = cv2.moments(redbinary,True)
# print(mymoment['m00'])
m00 = mymoment['m00']
m10 = mymoment['m10']
m01 = mymoment['m01']
middle_x = m10/m00
middle_y = m01/m00
end = time.clock()
print(middle_x,middle_y)
print(end - start)




