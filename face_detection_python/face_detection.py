import cv2
import numpy as np
import pandas as pd

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while(True):
    success, img = cap.read()
    faces = facedetect.detectMultiScale(img, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (w+x, y+h), (255, 0, 0))

    cv2.imshow("Frame", img)
    k = cv2.waitKey(1)
    if(k == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()
