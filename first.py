# segmentation based on intensity
import cv2
import numpy as np
image = cv2.imread('images/test.jpg', cv2.IMREAD_GRAYSCALE)
# image1 = cv2.imread('images/test.jpg', cv2.IMREAD_GRAYSCALE)


window = 'hi'
cv2.namedWindow(window,cv2.WINDOW_NORMAL)
cv2.resizeWindow(window,600,600)
cv2.moveWindow(window,0,0)

(d1,d2) = image.shape
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
        image1[m, k] = image[i, j]

print(image1[0,0,1])

cv2.imshow(window,image1)
cv2.waitKey(5000)
cv2.destroyAllWindows()