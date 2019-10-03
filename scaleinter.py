# scale image with interpolation
import cv2
import numpy as np
img0 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
# img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
# otpt = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

(d1, d2) = img0.shape
print(d1,d2)
img1 = np.zeros((d1,d2,3), np.uint8)
otpt = np.zeros((d1,d2,3), np.uint8)
img2 = np.zeros((d1,d2,3), np.uint8)
w1 = 'input'
w2 = 'output'
w3 = 'interpolated output'

cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

cv2.namedWindow(w3,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w3,400,400)
cv2.moveWindow(w3,400,0)


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
        if (ssy<d1 and ssx<d2):
            if(ssy>=0 and ssx>=0):
                img1[d1-1-ssy, ssx] = img0[d1-1-i, j]

for i in range (0 ,d1):
    for j in range (0, d2):
        otpt[i,j] = img1[i,j]
print(img1[0,0])
print(otpt[0,0])
for y in range (d1-2, 1, -1):
    for x in range (d2-2, 1, -1):
        # print('hi')
        if(img1[y,x,0]== 0 and img1[y,x,1]==0 and img1[y,x,2]==0):
            f = (int(img1[y+1, x-1, 0])+int(img1[y+1, x+1, 0])+int(img1[y-1, x-1, 0])+int(img1[y-1, x+1, 0]))/4
            otpt[y, x, 0] = f
            otpt[y, x, 1] = f
            otpt[y, x, 2] = f

# doing interpolation second time

for i in range (0 ,d1):
    for j in range (0, d2):
        img2[i,j] = otpt[i,j]
print(img1[0,0])
print(otpt[0,0])
for y in range (d1-2, 1, -1):
    for x in range (d2-2, 1, -1):
        # print('hi')
        if(img2[y,x,0]== 0 and img2[y,x,1]==0 and img2[y,x,2]==0):
            f = (int(img2[y+1, x-1, 0])+int(img2[y+1, x+1, 0])+int(img2[y-1, x-1, 0])+int(img2[y-1, x+1, 0]))/4
            otpt[y, x, 0] = f
            otpt[y, x, 1] = f
            otpt[y, x, 2] = f



print(type(i))
cv2.imshow(w1,img0)
cv2.imshow(w2,img1)
cv2.imshow(w3,otpt)
cv2.waitKey(0)
cv2.destroyAllWindows()