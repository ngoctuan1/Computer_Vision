# import numpy as np
# import cv2

# img = cv2.imread('shapes.png')
# output = img.copy()
# gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray, 5)

# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
#                            20, param1=100, param2=30, minRadius=0, maxRadius=0)
# detected_circle = np.uint16(np.around(circles))

# for (x, y, r) in detected_circle[0, :]:
#     cv2.circle(output, (x, y), r, (0, 255, 0), 3)
#     cv2.circle(output, (x, y), 2, (0, 255, 255), 3)

# cv2.imshow('output', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
from os.path import abspath

pathImg = abspath('../shapes.png')

img = cv2.imread(pathImg)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

circle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                          200, param1=100, param2=30, minRadius=0, maxRadius=0)
circle = np.uint16(np.around(circle))

# print(circle[0].shape)
print(circle.shape)      # [[[214  72  56]
                    #   [358 506  56]
                    #   [ 70 504  31]
                    #   [358 214  33]]]
for (x, y, r) in circle[0, :]:
    cv2.circle(img, (x, y), int(r), (0, 255, 0), 3)
    cv2.circle(img, (x, y), 2, (255, 255, 0), 3)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
