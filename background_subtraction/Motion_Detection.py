# import cv2
# import numpy as np
# from os.path import abspath

# pathImg = abspath('../background2.png')
# pathVideo = abspath('../test3.avi')

# cap = cv2.VideoCapture(pathVideo)
# background = cv2.imread(pathImg)
# bg_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
# bg_gray = cv2.GaussianBlur(bg_gray, (21, 21), 0)

# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# while True:
#     ret, frame = cap.read()

#     if frame is None:
#         break

#     # frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # frame_gray = cv2.GaussianBlur(frame_gray, (21, 21), 0)

#     # diff = cv2.absdiff(bg_gray, frame_gray)
#     # _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
#     # diff = cv2.dilate(diff, None,iterations=2)

#     diff = fgbg.apply(frame)
#     cnts, _ = cv2.findContours(
#         diff, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

#     for countour in cnts:
#         # if cv2.contourArea(countour) < 10500:
#         #     continue
#         x, y, w, h = cv2.boundingRect(countour)
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(25) == ord('1'):
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np
from os.path import abspath

pathImg = abspath('../shapes.png')
pathImg2 = abspath('../over.png')

img = cv2.imread(pathImg2)
img2 = cv2.imread(pathImg2)
# print(img.shape, img2.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                           150, param1=250, param2=20, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
# print(circles.shape)
for c in circles:
    x,y,r = c[0]
    cv2.circle(img, (x, y), r, (0, 255, 0), 3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
