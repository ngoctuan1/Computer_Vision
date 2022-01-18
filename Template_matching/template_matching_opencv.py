# import numpy as np
# import matplotlib as plt
# import cv2


# # def click_event(event, x, y, flags, param):
# #     if event == cv2.EVENT_LBUTTONDOWN:
# #         font = cv2.FONT_HERSHEY_SIMPLEX
# #         print(x, y)
# #         strXY = str(x) + ',' + str(y)
# #         cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
# #         cv2.imshow("image", img)


# img = cv2.imread("messi.jpeg")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# template = cv2.cvtColor(img[25:62, 245: 275], cv2.COLOR_BGR2GRAY)
# w, h = template.shape[::-1]

# res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF)
# print(res)
# threshold = 3423020
# loc = np.where(res >= threshold)
# print(loc)


# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
# cv2.imshow("image", img)
# # cv2.imshow('face', img[27:62, 249: 275])
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('messi.jpeg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img2 = img.copy()
template = cv.cvtColor(img[25:62, 245: 275], cv.COLOR_BGR2GRAY)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(imgGray, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img, top_left, bottom_right, 255, 2)
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
