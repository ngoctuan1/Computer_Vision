import cv2
import numpy as np
from os.path import abspath

pathVi = abspath('../highway.mp4')
cap = cv2.VideoCapture(pathVi)

# _, first_frame = cap.read()
# first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
# first_gray = cv2.GaussianBlur(first_gray, (5,5),0)
fgbg = cv2.createBackgroundSubtractorMOG2(history = 20, varThreshold=25)

while True:
    ret, frame = cap.read()

    if frame is None:
        break

    # frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame_gray = cv2.GaussianBlur(frame_gray, (5,5),0)
    

    # diff = cv2.absdiff(first_gray, frame_gray)
    # _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    # cv2.imshow('diff', diff)

    cv2.imshow('frame', frame)
    
    fgmask = fgbg.apply(frame)
    cv2.imshow('fgmask', fgmask)

    if cv2.waitKey(10) == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()
