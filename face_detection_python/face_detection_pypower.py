import numpy as np
import cv2
import os.path

pathImg = os.path.abspath('../face_detection_python/new/sample2.jpg')
pathFaceXml = os.path.abspath('../haarcascade_frontalface_default.xml')
pathEyeXml = os.path.abspath('../haarcascade_eye_tree_eyeglasses.xml')

face_detection = cv2.CascadeClassifier(pathFaceXml)
eye_detection = cv2.CascadeClassifier(pathEyeXml)

img = cv2.imread(pathImg)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_detection.detectMultiScale(gray, 1.2, 6)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    roi_gray = gray[y:y+h, x:x+w]
    roi_img = img[y:y+h, x:x+w]
    eyes = eye_detection.detectMultiScale(roi_gray)

    for ex, ey, ew, eh in eyes:
        cv2.rectangle(roi_img, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
