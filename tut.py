import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLORMAP_JET)

    # Display the resulting frame

    #time.sleep(1.5)
    print((gray[0][1]))
    for i in range(0,350):
        for j in range(0,600):
            gray[i][j] = [0,0,0,255]
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
