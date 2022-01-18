import cv2
import numpy as np
from os.path import abspath

pathCap = abspath('../testvideo2.mp4')

cap = cv2.VideoCapture(pathCap)

FOI = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)

# create an array of frame from frames chosen above
frames = []

for frameOI in FOI:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
    ret, frame = cap.read()
    frames.append(frame)
# calculate the average
bg_frame = np.median(frames, axis=0).astype(dtype= np.uint8)

cv2.imshow('bg_frame', bg_frame)
# cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(len(frames))