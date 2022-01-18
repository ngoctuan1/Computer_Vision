import cv2
import numpy as np

img = cv2.imread("gradient.png", 0)

# 127 sẽ là ranh giới để phân chia
# nếu pixel < 127 thì 0 > 127 là 1 ( Theo cv2.THRESH_BINARY)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

# cv2.THRESH_BINARY_INV sẽ ngược lại vs cái trên
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

# cv2.THRESH_TRUNC sẽ tính theo ranh giới
#  vd: 127 là ranh giới thì < 127 sẽ giữ nguyên px
#  > 127 sẽ = 127
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# cv2.THRESH_TOZERO , nếu < ranh giới = 0
# > ranh giới sẽ giữ nguyên

_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
