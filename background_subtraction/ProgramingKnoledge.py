import cv2
import numpy as np
from os.path import abspath

pathImg = abspath('../vtest.avi')
video = cv2.VideoCapture(pathImg)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# fgbg2 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
# fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg4 = cv2.createBackgroundSubtractorKNN()

while True:

    ret, frame = video.read()
    if frame is None:
        break

    fgmask = fgbg4.apply(frame)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('FG Mask', fgmask)

    if cv2.waitKey(25) == ord('1'):
        break

video.release()
cv2.destroyAllWindows()
