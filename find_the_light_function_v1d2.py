#-*-coding:utf-8-*-
#code by yyt
#version1.0
    # 1.从文件夹中读取图像
    # 2.调整分辨率(shrink)
    # 3.提取红色部分(pick the red block)
    # 4.提取黑色部分(pick the blakc blokc)
    # 5.一阶矩获取中心点
#version1.1
    #加入了获取障碍物方位
#version1.2
    #封装成函数


import cv2
import numpy as np
import numpy
import time

##分辨率转换
def shrink_img(img,height,width):
    size = (width,height)
    return cv2.resize(img,size,cv2.INTER_AREA)

##BRG转HSV
def change_hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

##选取红色
def pick_red(img):
    redlower = np.array([150, 80, 80])
    redupper = np.array([179, 255, 255])
    return cv2.inRange(img,redlower,redupper)

##选取黑色
def pick_black(img):
    blacklower = np.array([0, 0, 9])
    blackupper = np.array([180, 255, 46])
    return cv2.inRange(img, blacklower, blackupper)

##二值化
#阈值thresh
#最大值max
def change_binary(img):
    thresh = 120
    max = 255
    ret1,binary = cv2.threshold(img,thresh,max,cv2.THRESH_BINARY)
    return binary

##求重心
def get_center(img):
    mymoment = cv2.moments(img,True)
    m00 = mymoment['m00']
    m10 = mymoment['m10']
    m01 = mymoment['m01']
    middle_x = m10 / m00
    middle_y = m01 / m00
    center = [middle_x,middle_y]
    return center

##从原始图片到中心点
def raw2center(img):
    img = change_hsv(img)
    img = pick_red(img)
    img = change_binary(img)
    return get_center(img)

#img = cv2.imread("g:/samples/test11.jpg")
#img = shrink_img(img,372,496)
# img = change_hsv(img)
# cv2.imshow('1',pick_red(img))
# cv2.waitKey()
# img = pick_red(img)
# img = change_binary(img)
# cv2.imshow('2',img)
# cv2.waitKey()
# center = get_center(img)
#print(raw2center(img))
# print(img.shape)