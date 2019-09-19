import cv2
import numpy as np
image = cv2.imread('images/test.jpg')
# image1 = cv2.imread('images/test.jpg', cv2.IMREAD_GRAYSCALE)


window = 'hi'
cv2.namedWindow(window,cv2.WINDOW_NORMAL)
cv2.resizeWindow(window,600,600)
cv2.moveWindow(window,0,0)

(d1,d2,d3) = image.shape
print(d1,d2)
m = d1
k = d2
image1 = np.zeros((d1,d2,3), np.uint8)
print(image1.shape)
print(image1[0,0])

for i in range (0,d1):
    m = d1-i-1
    for j in range (0,d2):
        k = d2-j-1
        image1[m, k, 0] = image[i, j, 0]
        image1[m, k, 1] = image[i, j, 1]
        image1[m, k, 2] = image[i, j, 2]
print(image1[0,0,1])
print(image[0,0,1])

cv2.imshow(window,image1)
cv2.waitKey(5000)
cv2.destroyAllWindows()