import cv2
import numpy as np
from joining_images import stackImages

def getContours(img):
    contours,hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgContour, cnt,-1,(255,0,0),3)


path = "shapes.png"

img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)

imgStack = stackImages(0.6, ([img, imgGray, imgBlur], [
                       imgCanny, imgContour, imgBlank]))

cv2.imshow("Output", imgStack)


cv2.waitKey(0)
