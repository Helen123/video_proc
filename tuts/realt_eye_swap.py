# Bad exprmnt on swapping eyes in real time.
import numpy as np
import cv2
import time

def eye_swap(roi_color,eyes):
    if len(eyes)<2:
        return
    eye1 = eyes[0]
    eye1_co={}
    eye1_co['x']=eye1[0]
    eye1_co['y'] = eye1[1]
    eye1_co['w'] = eye1[2]
    eye1_co['h']=eye1[3]


    eye2 = eyes[1]
    eye2_co = {}
    eye2_co['x'] = eye2[0]
    eye2_co['y'] = eye2[1]
    eye2_co['w'] = eye2[2]
    eye2_co['h'] = eye2[3]

    # for (ex, ey, ew, eh) in eyes:
    #    # cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    #
    tx=0
    ty=0
    for i in range(eye1_co['x'],eye1_co['x']+eye1_co['w']):
        i2 = eye2_co['x'] + tx
        for j in range(eye1_co['y'],eye1_co['y']+eye1_co['h']):
            j2=eye2_co['y'] +ty
            if i2<len(roi_color) and j2<len(roi_color[i2]):
                roi_color[i][j],roi_color[i2][j2] = roi_color[i2][j2],roi_color[i][j]
        ty+=1
        tx+=1
    # for i in range(eye1_co['y'],eye1_co['y']+eye1_co['h']):
    #     j = eye2_co['y']+i
    #     roi_color[i],roi_color[j] = roi_color[j],roi_color[i]
    return roi_color

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, img = cap.read()
    #img = cv2.imread('slaxk.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('img', img)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        eye_swap(roi_color,eyes)
    cv2.imshow('img',img)
    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

