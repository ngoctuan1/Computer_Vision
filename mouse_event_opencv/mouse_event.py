import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # ----------------1--------------
        print(x, " ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2)

        # ---------------2-------------
        # cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

        # # Khi click vào vị trí bất kì thì thêm vào mảng
        # points.append((x, y))

        # # Kiểm tra xem len của mảng đủ để tạo thành 1 đường thẳng 2 ko
        # if len(points) >= 2:
        #     # Vẽ 1 đường thẳng theo 2 điểm cuối
        #     cv2.line(img, points[-1], points[-2], (0, 0, 255), 5)

        # ------------------3-------------
        # blue = img[x, y, 0]
        # green = img[x, y, 1]
        # red = img[x, y, 2]
        # cv2.circle(img, (x, y), 3, (0, 0, 0), -1)
        # mycolorImg = np.zeros((512, 512, 3), np.uint8)

        # mycolorImg[:] = [blue,green,red]


        # cv2.imshow("color", mycolorImg)

    # Thể hiện màu theo bgr bit khi right click
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[y,x,0]
    #     green = img[y,x,1]
    #     red = img[y,x,2]
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strBGR = str(blue) + ' , ' + str(green) + " , " + str(red)
    #     cv2.putText(img, strBGR, (x, y), font, .5, (0, 0, 0), 2)
    #     cv2.imshow("image", img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("shapes.png")
cv2.imshow("image", img)
points = []
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(events)
