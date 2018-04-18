import find_the_light_function_v1d2
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
    ret,frame = cap.read()
    num += 1
    center = find_the_light_function_v1d2.raw2center(frame)
    print(center)
    if (num == 300):
        # print(ord('0'))
        break

end1 = time.clock()
end2 = time.time()
print(num)
real_time_use = end2 - start2
print(end1 - start1)
print(real_time_use)
print(num/real_time_use)