#doubt
import cv2
import numpy as np
img=cv2.imread(r'messi5.jpg')
#img=cv2.rectangle(img,(10,30),(90,100),(63,75,74),6)
ball=img[280:340,330:390]
print(ball)
img[273:333,100:160]=ball
cv2.imshow('image1',ball)
cv2.imshow('image',img)

k=cv2.waitKey(0)
if k==ord('a'):
   cv2.destroyAllWindows()
