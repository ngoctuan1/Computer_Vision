import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
cv.namedWindow("Tracker")


def nothing(x):
    pass


cv.createTrackbar("LowHue", "Tracker", 0, 255, nothing)
cv.createTrackbar("UpHue", "Tracker", 255, 255, nothing)
cv.createTrackbar("LowSae", "Tracker", 0, 255, nothing)
cv.createTrackbar("UpSae", "Tracker", 255, 255, nothing)
cv.createTrackbar("LowVal", "Tracker", 0, 255, nothing)
cv.createTrackbar("UpVal", "Tracker", 255, 255, nothing)

while True:
    # frame = cv.imread("smarties.png")

    _, frame = cap.read()
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LowHue", "Tracker")
    u_h = cv.getTrackbarPos("UpHue", "Tracker")

    l_s = cv.getTrackbarPos("LowSae", "Tracker")
    u_s = cv.getTrackbarPos("UpSae", "Tracker")

    l_v = cv.getTrackbarPos("LowVal", "Tracker")
    u_v = cv.getTrackbarPos("UpVal", "Tracker")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv.inRange(frame_hsv, l_b, u_b)
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    k = cv.waitKey(1)
    if k == ord("1"):
        break

cap.release()
cv.destroyAllWindows()
