import numpy as np
import cv2



img = cv2.imread("shapes.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, threshold = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# print(len(contours))N
# print(contours[0])

cv2.drawContours(img, contours, -1,(255,255,0),3)

cv2.imshow("image", img)
cv2.imshow("imageGray", imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
    - Contours is a Python list of all the contours in the
        image. Each individual contours is a Numpy array
        of (x,y) coordinates of boundary points of the object
    - Hierarchy is the optional output vector  which is 
        containing the information about image topology 
"""
