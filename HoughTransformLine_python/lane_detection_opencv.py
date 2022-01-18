import matplotlib.pyplot as plt
import cv2
import numpy as np


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[-1]
    # match_mask_color = (255,) * channel_count
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_the_lines(img, lines):
    imgCopy = np.copy(img)
    blank_img = np.zeros(img.shape, dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_img, (x1, y1), (x2, y2), (255, 255, 0), 4)

    img = cv2.addWeighted(img, 0.8, blank_img, 1, 0)
    return img


# img = cv2.imread('road.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def process(img):

    h, w = img.shape[0:2]

    resion_of_interest_vertices = [
        (0, h),
        (w/2, h/2),
        (w, h)
    ]

    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_img = cv2.Canny(gray_image, 100, 120)

    cropped_image = region_of_interest(
        canny_img, np.array([resion_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 50,
                            lines=np.array([]), minLineLength=40, maxLineGap=100)

    drop_lines = draw_the_lines(img, lines)
    return drop_lines


cap = cv2.VideoCapture('test2.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()


# def region_of_interest(img, vertices):
#     mask = np.zeros_like(img)
#     # channel = img.shape[2]
#     # mask_color = (255, ) * channel
#     mask_color = 255
#     cv2.fillPoly(mask, vertices, mask_color)
#     img = cv2.bitwise_and(mask, img)
#     return img


# def draw(img, lines):
#     imgCopy = img.copy()
#     blank_img = np.zeros(img.shape, dtype=np.uint8)

#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         cv2.line(imgCopy, (x1, y1), (x2, y2), (0, 255, 0), 3)

#     img = cv2.addWeighted(blank_img, .8, imgCopy, 1, 0)
#     return img


# img = cv2.imread('road.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# h, w = img.shape[0:2]

# region_of_interest_vertices = [
#     (0, h),
#     (w / 2, h / 2),
#     (w, h)
# ]

# imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# imgCanny = cv2.Canny(imgGray, 100, 200)

# cropped_img = region_of_interest(imgCanny, np.array(
#     [region_of_interest_vertices], np.int32))

# lines = cv2.HoughLinesP(cropped_img, 6, np.pi / 180, 160, np.array([]), 40, 25)

# draw_line = draw(img, lines)

# plt.imshow(draw_line)
# plt.show()
