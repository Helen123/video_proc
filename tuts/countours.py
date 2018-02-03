import numpy as np
import cv2
import time
im = cv2.imread('test.png')
# cv2.imshow('frame',im)

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# time.sleep(5)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy  = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
maxi=0
i_max=0
for i in range(0,len(contours)):
   if cv2.contourArea(contours[i])>maxi:
       maxi = cv2.contourArea(contours[i])
       i_max=i

im_final = cv2.drawContours(im, contours, -1, (255,0,0), 3)
while(True):
    cv2.imshow("frame",im_final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break