import cv2
import numpy as np
img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

(d1,d2) = img1.shape
print(d1,d2)

mask = np.zeros((3,1,3), np.uint8)
otpt = np.zeros((d1,d2,3), np.uint8)

w1 = 'input'
w2 = 'output'

cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)
