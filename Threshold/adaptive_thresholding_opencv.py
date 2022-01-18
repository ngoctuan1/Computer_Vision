import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.png", 0)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 2)

th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

title = ["image", "th1", "th2", "th3"]
image = [img, th1, th2, th3]

for index, (im, tit) in enumerate(zip(image, title)):
    plt.subplot(2, 2,index+ 1)
    plt.title(tit)
    plt.imshow(im,"gray")
    plt.xticks([])
    plt.yticks([])

plt.show()
# cv2.imshow("image", img)
# cv2.imshow("th1", th1)
# cv2.imshow("th2", th2)
# cv2.imshow("th3", th3)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
