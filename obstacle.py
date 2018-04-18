#-*-coding:utf-8-*-
#code by yyt
#version_beta
    #1.寻找1,2,3,4区域是否有障碍
    #2.判断是否有障碍方法：对一块区域求黑色像素点个数




import numpy
import cv2
import numpy as np
import find_the_light_function_v1d2
import pandas as pd

##取数组并对像素点求和
##para:
    #beginline,beginrow:开始行，开始列
    #height,width:总行数，列数
def pick_and_sum(img,beginline,beginrow,height,width):
    ROI = img[beginline:beginline+height,beginrow:beginrow+width]
    sum255 = np.sum(ROI)
    sum = sum255/255
    print(ROI)
    return sum

##导出数据到excel表格
def export_to_excel(img):
    data_df = pd.DataFrame(img)
    # print(type(data_df))
    writer = pd.ExcelWriter('g:/samples/dataexcel.xlsx')
    data_df.to_excel(writer,'page_1')
    writer.save()
    return


#test
# b = np.array([[1,2,3],[1,3,4]])
# sum1 = np.sum(b)
# print b.shape

img = cv2.imread("g:/samples/test11.jpg")
img = find_the_light_function_v1d2.shrink_img(img,49,37)
#print(img)
img = find_the_light_function_v1d2.change_hsv(img)
img = find_the_light_function_v1d2.pick_black(img)
img = find_the_light_function_v1d2.change_binary(img)
cv2.imshow("show",img)
cv2.waitKey()
# np.set_printoptions(threshold=49*37)
# print(img)
sum1 = pick_and_sum(img,34,0,3,10)
print(sum1)


