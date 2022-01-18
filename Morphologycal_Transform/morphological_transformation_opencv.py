import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# loại bỏ các chấm đen từ mask
kernel = np.ones((5, 5), np.uint8)
# giản nở (Dùng để làm mất đi những cái gây nhiễu bên trong vật thể)
dialation = cv2.dilate(img, kernel, iterations=2)
# xói mòn (Dùng để làm mất đi bên ngoài vật thể)
erosion = cv2.erode(img, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
mg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# It is the difference between input image and Opening of the image
th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# It is the difference between the closing of the input image and input image
bh = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT, kernel)

titles = ["image", "mask", "dialation",
          "erosion", "opening", "closing", "mg", "th"]
images = [img, mask, dialation, erosion, opening, closing, mg, th]

for index, (img, title) in enumerate(zip(images, titles)):
    plt.subplot(3, 3, index+1)
    plt.imshow(img, "gray")
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
plt.show()
