import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("messi.jpeg")

# -------------------Gaussian---------------------
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow("upper", layer)
lp = [layer]

for i in range(5, 0, -1):
    size = (gp[i - 1].shape[1], gp[i - 1].shape[0])
    gaussian_ex = cv2.pyrUp(gp[i], dstsize=size)
    # print(gp[i-1].shape, '--', gaussian_ex.shape)
    lap = cv2.subtract(gp[i-1], gaussian_ex)

    cv2.imshow(str(i), lap)


cv2.waitKey(0)
cv2.destroyAllWindows()


"""
    - Pyramid, or pyramid representation, is a type of
        multi-scale signal representation in which
        a signal or an image is subject to repeated 
        smoothing and subsampling

    ** INCLUDE:
        1.Gaussian Pyramid
        2.Laplacian Pyramid

    - A level in Laplacian Pyramid is formed by the 
        difference between that level in Gaussian Pyramid
        and expanded version of its upper level in
        Gaussian Pyramid

"""
