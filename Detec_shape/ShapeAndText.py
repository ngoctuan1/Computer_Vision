import cv2
import numpy as np

# Tạo 1 frame có width = 512, height = 520
img = np.zeros((512,512,3),np.uint8)
# img[10:20,100:300] = 250,0,0
#                 width,height
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,250,0),2)

# Tạo tứ giác     điểm đầu, điểm cuối, color, độ dày      
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)

# Tạo hình tròn trọng tâm, bán kính, color, độ dày
# Kc của hình vs viền của frame  = trọng tâm - bán kình
cv2.circle(img,(400,50),40,(255,255,0),5)

# Tạo chữ cho frame
cv2.putText(img,"OPEN CV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()