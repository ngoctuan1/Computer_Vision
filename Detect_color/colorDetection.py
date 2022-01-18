import cv2
import numpy as np


def empty(a):
    pass


path = "nuochoa.jpg"

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 240)

cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBar", 34, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 13, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 111, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 92, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    imgResult = cv2.bitwise_and(img,img,mask = mask)

    # cv2.imshow("Output", img)
    cv2.imshow("Output1", img)
    cv2.imshow("Output2", mask)
    cv2.imshow("Output3", imgResult)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

