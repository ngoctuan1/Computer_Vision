"""
    -----------Hough Transform Basics---------------
    - The Hough Transform is a popular technique to
        detect any shape, if you can represent that shape
        in a mathematical form. It can detect the shape
        even if it broken or distorted a little bit


    - A line in the image space can be expressed with two
        variables. For example:
        * In the Cartesian coordinate system yi = m*xi + can
        * In the Polar coordinate system  x*cos0 + y*sin0 = r

    -----------------Hough Transform Algorithm-------------
    1. Edge detection, e.g. using the Canny edge detector

    2. Mapping of edge points to the Hough space and
        storage in an accumulator
        (Ánh sạ các điểm cạnh tới không gian Hough và lưu trữ
        trong bộ tích lũy)

    3. Interpretation of the accumulator to yield lines of
        infinite length. The interpretation is done by
        thresholding and possibly other constraints
        (Diễn dịch các bộ tích lũy để mang lại các dòng có
        độ dài vô hạn. Việc diễn dịch được thực hiện bởi
        ngưỡng và có thể là các ràng buộc khác)

    4. Conversion of infinite lines to finite lines
        (Chuyển các dòng vô hạn thành hữu hạn)

    -------OpenCV implements two kind of Hough Line Transform------

    1. The Standard Hough Transform(HoughLines method)
    2. The Probabilistic Hough Line Transform (HoughLinesP method)
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
from os.path import abspath

pathImg = abspath('../sudoku.png')
img = cv2.imread(pathImg)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
# edges2 = cv2.Canny(gray, 50, 150 )

lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
# lines2 = cv2.HoughLines(edges2,1, np.pi/180, 200)

for line in lines:
    # line = [[361.          1.5707964]]
    # * rho is the distance from the coordinate zero (0,0)
    #   which is the top-left corner of the image

    # * theta is the line rotation angle in radians
    rho, theta = line[0]

    a = np.cos(theta)
    b = np.sin(theta)

    x0 = a * rho
    y0 = b * rho

    # x1 stores the rounded off value off ( r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))

    # y1 stores the rounded off value off ( r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))

    # x2 stores the rounded off value off ( r * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))

    # y2 stores the rounded off value off ( r * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("image2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
