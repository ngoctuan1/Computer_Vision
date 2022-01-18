import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Noise_salt_and_pepper.png", 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 10)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', "2D", 'blur', 'gaussian blur', 'median blur', 'bilate']
images = [img, dst, blur, gblur, median,bilateral]

for index, (img, title) in enumerate(zip(images, titles)):
    plt.subplot(2, 3, index+1)
    plt.imshow(img, "gray")
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
plt.show()


"""
    - Homogeneous filter, Gaussian filter, Median filter
         Bilateral Filter

    - Homogeneous filter is the most simpe filter, each output
         pixel is the mean of its kernel neighbors

    - IN image processing, a kernel convolution matrix, or mask
        is a small matrix, It is used for blurring, sharpening(sắc nét)
        , embossing(), edge detection(phát hiện cạnh), and more

    - As in one-dimensional signals, images also can be 
        filtered with various low-pass filters(LPF),
        high-pass filters(HPS) etc
    - LBF helps on removing noises, blurring the images
    - HPF filters helps on finding edges in the images

    - Gaussian filter is nothing but using different-wright-kernel
    , in both x and y direction
            1 / 16 * [[1  4  6  4 1],
                      [4 16 24 16 4],
                      [6 24 36 24 6],
                      [4 16 24 16 4],
                      [1  4  6  4 1]]

    - Median filter is something that replace each pixel's
        value with the median of its neighboring pixels.
        This method is great when dealing with "salt and pepper
        noise"
"""
