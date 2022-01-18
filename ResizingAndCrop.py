import cv2

img = cv2.imread("nuochoa.jpg")
# => (428, 427, 3) :
# 428 là width,
# 428 là height,
# 3 là hiện thị theo số kênh BGF
print(img.shape)

imgResize = cv2.resize(img, (300, 300))

# Cắt hình theo tỉ lệ
# Do hình gốc có kích thước (428, 427) => (0->428 , 0 -> 427)
# 100:200 là height, 200:300 là width
imgCropped = img[100:200, 200:300]

cv2.imshow("Output", img)
# cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)
