import cv2
import numpy as np
import imgae_stack as st


def print_hsv(b, g, r):
    img1 = np.uint8([[[b, g, r]]])
    print(cv2.cvtColor(img1, cv2.COLOR_BGR2HSV))
    


def show(b, g, r):
    img = cv2.imread("shapes.png", 1)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    min_mau = np.array([b-1, g, r])
    max_mau = np.array([b+1, g, r])
    mask_img = cv2.inRange(img_hsv, min_mau, max_mau)
    final = cv2.bitwise_and(img, img, mask=mask_img)

    cv2.imshow("Ouput", st.stackImages(0.6, [img, img_hsv, mask_img, final]))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


print_hsv(0, 241, 255)
show(28,255,255)
