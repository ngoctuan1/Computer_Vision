import numpy as np
import cv2
import sys
from os.path import abspath


def resize(dst, img):
    h, w = img.shape[0:2]

    dim = (w, h)
    resized = cv2.resize(dst, dim, interpolation=cv2.INTER_AREA)
    return resized

pathCap = abspath('../ocean.mp4')

cap = cv2.VideoCapture(0)
oceanCap = cv2.VideoCapture(pathCap)
_, ref_img = cap.read()
flag = 0

while True:
    _, img = cap.read()
    _, bg = oceanCap.read()
    bg = resize(bg, ref_img)
    if flag == 0:
        ref_img = img

    # create a mask
    diff1 = cv2.subtract(img, ref_img)
    diff2 = cv2.subtract(ref_img, img)
    diff = diff1 + diff2

    diff[abs(diff) < 13.0] = 0
    gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    gray[np.abs(gray) < 10] = 0
    fg_mask = gray.astype(np.uint8)
    fg_mask[fg_mask > 0] = 255

    # inverse the fg_mask
    fg_mask_inv = cv2.bitwise_not(fg_mask)

    # use the masks to extract the relevant parts from FG and BG
    fg_img = cv2.bitwise_and(img, img, mask=fg_mask)
    bg_img = cv2.bitwise_and(bg, bg, mask=fg_mask_inv)

    # combine both the BG and the FG images
    dst = cv2.add(bg_img, fg_img)
    cv2.imshow('bg_remove', dst)

    k = cv2.waitKey(5)
    if k == ord('1'):
        break
    elif k == ord('d'):
        flag = 1
        print('bg_captured')
    elif k == ord('r'):
        flag = 0
        print('ready to capture new background')

cv2.destroyAllWindows()
cap.release()
