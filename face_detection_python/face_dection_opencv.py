"""
    first, a classifier (namely a cascade of boosted classifier
    working with haar-like feature) is trained with a few hundred
    sample views of a particular object(i.e., a face or a car),
    called positive examples, that are scaled to the same size
    (say, 20x20) and negative examples- arbitrary images of 
    the same size
"""
import numpy as np
import cv2

img = cv2.imread('about_img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_detection.detectMultiScale(gray, 1.1, 3)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
