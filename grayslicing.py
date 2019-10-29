# gray level slicing
import cv2
import numpy as np

img = cv2.imread("images/test.jpg",cv2.IMREAD_GRAYSCALE)

(d1, d2) = img.shape

otpt = np.zeros((d1,d2,1), np.uint8)

w1 = 'input'
w2 = 'output'

cv2.namedWindow(w1,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)


r1 = int(input("grey level\nlower limit "))
r2 = int(input("uppper limit "))

for i in range(0, d1):
    for j in range (0, d2):
        if(img[i,j] >= r1 and img[i,j] <= r2):
            otpt[i,j] = 255

cv2.imshow(w1,img)
cv2.imshow(w2,otpt)
cv2.waitKey(0)
cv2.destroyWindow()