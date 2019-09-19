import cv2
import numpy as np
img = cv2.imread('images/test.jpg')
print('IMAGE SIZE ',img.shape)
w1 = 'input'
w2 = 'output'
# cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
# cv2.resizeWindow(w1,300,300)
# cv2.moveWindow(w1,0,0)

# cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
# cv2.resizeWindow(w2,300,300)
# cv2.moveWindow(w2,0,300)

res = cv2.resize(img, None , fx=1, fy=.5, interpolation = cv2.INTER_CUBIC)
print('NEW IMAGE SIZE ',res.shape)

# cv2.imshow(w1,img)
cv2.imshow(w2,res)
cv2.waitKey(5000)
cv2.destroyAllWindows()