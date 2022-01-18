# import cv2
# import numpy as np
# import matplotlib.pyplot as plt


# def nothing(x):
#     pass


# cap = cv2.VideoCapture('road_car_view.mp4')
# cv2.namedWindow("TrackBar")
# cv2.createTrackbar("MinHue", "TrackBar", 0, 255, nothing)
# cv2.createTrackbar("MaxHue", "TrackBar", 255, 255, nothing)
# cv2.createTrackbar("MinSae", "TrackBar", 0, 255, nothing)
# cv2.createTrackbar("MaxSae", "TrackBar", 255, 255, nothing)
# cv2.createTrackbar("MinVal", "TrackBar", 0, 255, nothing)
# cv2.createTrackbar("MaxVal", "TrackBar", 255, 255, nothing)
# # while True:
# #     ret, orig_frame = cap.read()
# #     if not ret:
# #         cap = cv2.VideoCapture('road_car_view.mp4')
# #         continue

# #     frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
# #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# #     min_hue = cv2.getTrackbarPos("MinHue", "TrackBar")
# #     max_sae = cv2.getTrackbarPos("MaxSae", "TrackBar")
# #     min_sae = cv2.getTrackbarPos("MinSae", "TrackBar")
# #     max_hue = cv2.getTrackbarPos("MaxHue", "TrackBar")
# #     min_val = cv2.getTrackbarPos("MinVal", "TrackBar")
# #     max_val = cv2.getTrackbarPos("MaxVal", "TrackBar")

# #     # low_yellow = np.array([18, 94, 140])
# #     # up_yellow = np.array([48, 255, 255])
# #     lower = np.array([min_hue, min_sae, min_val])
# #     upper = np.array([max_hue, max_sae, max_val])
# #     mask = cv2.inRange(hsv, lower, upper)

# #     # edges = cv2.Canny(mask, 75, 150)
# #     # lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)

# #     # if lines is not None:
# #     #     for line in lines:
# #     #         x1, y1, x2, y2 = line[0]
# #     #         cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

# #     # cv2.imshow('frame', frame)
# #     cv2.imshow('mask', mask)
# # if cv2.waitKey(0) == ord('1'):
# #     break


# ret, frame = cap.read()
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


# while True:
#     min_hue = cv2.getTrackbarPos("MinHue", "TrackBar")
#     max_sae = cv2.getTrackbarPos("MaxSae", "TrackBar")
#     min_sae = cv2.getTrackbarPos("MinSae", "TrackBar")
#     max_hue = cv2.getTrackbarPos("MaxHue", "TrackBar")
#     min_val = cv2.getTrackbarPos("MinVal", "TrackBar")
#     max_val = cv2.getTrackbarPos("MaxVal", "TrackBar")
#     lower = np.array([min_hue, min_sae, min_val])
#     upper = np.array([max_hue, max_sae, max_val])
#     mask = cv2.inRange(hsv, lower, upper)
#     cv2.imshow('mask', mask)
#     if cv2.waitKey(1) == ord('1'):
#         break


# # cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt


def Canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def region_of_interest(image):
    mask = np.zeros_like(image)
    h, w = image.shape[0:2]
    polygons = [(200, h), (550, h / 2), (w, h)]
    cv2.fillPoly(mask, np.array([polygons], np.int32), 255)

    masked_img = cv2.bitwise_and(image, mask)
    return masked_img


def draw_image(image, lines):
    mask = np.zeros_like(image)

    if(lines is not None):
        for x1, y1, x2, y2 in lines:
            cv2.line(mask, (x1, y1), (x2, y2), (0, 255, 0), 10)

    image = cv2.addWeighted(image, .8, mask, 1, 1)
    return image


def averate_slope_intercept(image, lines):
    left_fit = []
    right_fit = []

    for line in lines:
        x1, y1, x2, y2 = line[0]
        parameter = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameter[0]
        intercept = parameter[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))

    left_fit_average = np.mean(left_fit, axis=0, dtype=np.float32)
    right_fit_average = np.mean(right_fit, axis=0, dtype=np.float32)

    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)

    return np.array([left_line, right_line])


def make_coordinates(image, line_parameters):
    print(line_parameters)
    slope, intercept = line_parameters
    y1 = image.shape[0]
    # 3/5 là chia hình ảnh thành 3/5 phần
    y2 = int(y1 * (3/5))

    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    # nó phải cùng vs x1, y1, x2, y2 = line[0]
    return np.array([x1, y1, x2, y2])


def process(img):
    imgCopy = img.copy()
    canny = Canny(imgCopy)
    cropped = region_of_interest(canny)
    lines = cv2.HoughLinesP(cropped, 2, np.pi/180, 100,
                            np.array([]), minLineLength=40, maxLineGap=5)

    averate_line = averate_slope_intercept(imgCopy, lines)
    drawed = draw_image(imgCopy, averate_line)
    return drawed


cap = cv2.VideoCapture('test2.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        ret, frame = cap.read()

    frame = process(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()
