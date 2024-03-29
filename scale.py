# scaling an image
import cv2
import numpy as np
img0 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
# img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)


(d1, d2) = img0.shape
print(d1,d2)
img1 = np.zeros((d1,d2,3), np.uint8)
w1 = 'input'
w2 = 'output'
cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

print(type(d1))

px = int(input('enter the x value of pivot:'))
py = int(input('enter the y value of pivot:'))
sx = int(input('enter scaling factor for x :'))
sy = int(input('enter scaling factor for y :'))

# for i in range (0 ,d1):
#     for j in range (0, d2):
#         img1[i,j] = 0

for i in range (0, d1):
    ssy = ((i-py)*sy)+py
    # print(i,ssx)
    for j in range (0, d2):
        ssx = ((j-px)*sx)+px
        if (ssx<d2 and ssy<d1):
            if(ssx>=0 and ssy>=0):
                img1[d1-ssy-1, ssx] = img0[d1-i-1, j]
print(type(i))
cv2.imshow(w1,img0)
cv2.imshow(w2,img1)
cv2.waitKey(0)
cv2.destroyAllWindows()