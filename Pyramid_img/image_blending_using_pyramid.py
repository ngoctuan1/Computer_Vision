import numpy as np
import cv2
import matplotlib.pyplot as plt


def show(image, title, cmap="Greys_r"):
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.show()

apple = cv2.imread("apple.jpg")
apple = cv2.cvtColor(apple, cv2.COLOR_BGR2RGB)
orange = cv2.imread("orange.jpg")
orange = cv2.cvtColor(orange, cv2.COLOR_BGR2RGB)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# generate Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)


# generate Gaussian pyramid for apple
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)


# generate Laplacian Pyramid for apple
apple_copy = gp_apple[-1]
lp_apple = [apple_copy]

for i in range(6, 0, -1):
    # size = gp_apple[i-1].shape[0:2]
    gaussian_ex = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_ex)
    lp_apple.append(laplacian)
    

# generate Laplacian Pyramid for apple
orange_copy = gp_orange[-1]
lp_orange = [orange_copy]

for i in range(6, 0, -1):
    # size = gp_orange[i-1].shape[0:2]
    gaussian_ex = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i - 1], gaussian_ex)
    lp_orange.append(laplacian)

# Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack(
        (apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)


# for i in range(7):
#     show(apple_orange_pyramid[i], '')
#  now reconstruct
apple_orange_re = apple_orange_pyramid[0]
for i in range(1, 7):
    size = apple_orange_pyramid[i].shape[0:2]
    # print(apple_orange_pyramid[i].shape,'---',apple_orange_re.shape)
    apple_orange_re = cv2.pyrUp(apple_orange_re, dstsize=None)
    apple_orange_re = cv2.add(apple_orange_pyramid[i], apple_orange_re)
    show(apple_orange_pyramid[i], 're')


# cv2.imshow("apple", apple)
# cv2.imshow("orange", orange)
# cv2.imshow("apple_orange", apple_orange)
# cv2.imshow("apple_orange_reconstruct", apple_orange_re)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""
    - To blend two images using image pyramids technique
        we need to follow five step:

        1. Load the two images of apple and orange
        2. Find the Gaussian Pyramids for apple and orange
            (in this particular example, number of
            level is 6)
        3. From Gaussia Pyramids, find their Laplacian Pyramids
        4. Now join the left half of apple and right half of
            orange in each levels of Laplacuan Pyramids 
        5. Join these images Pyramid and reconstruct to original images

"""
