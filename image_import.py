import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FPS,5)
num = 0

start1 = time.clock()
start2 = time.time()
while True:
    #get a frame
    ret,frame = cap.read()
    num +=1
    # print(frame.shape)

    cv2.imshow("capture",frame)
    if(cv2.waitKey(10) == ord('0')):
        # print(ord('0'))
        break
end1 = time.clock()
end2 = time.time()
print(num)
real_time_use = end2 - start2
print(end1 - start1)
print(real_time_use)
print(num/real_time_use)
# print(type(frame))
