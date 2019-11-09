# image rotation
import cv2
import math
img0 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

(d2, d1) = img0.shape
print(d1,d2)

w1 = 'input'
w2 = 'output'
cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

print(type(d1))

xr = int(input('enter the x value of pivot:'))
yr = int(input('enter the y value of pivot:'))
ang = int(input('enter the angle :'))

for i in range (0 ,d2):
    for j in range (0, d1):
        img1[i,j] = 0

for i in range (0, d2):
    # print(i,ssx)
    for j in range (0, d1):
        xxr = int(xr+((j-xr)*math.cos(ang*(math.pi/180)))-(((i)-yr)*math.sin(ang*(math.pi/180))))
        yyr = int(yr+((j-xr)*math.sin(ang*(math.pi/180)))+(((i)-yr)*math.cos(ang*(math.pi/180))))
        # print("x=", j, "x'=", xxr, "y=", i," y'=", yyr)
        if (yyr<d2 and xxr<d1):
            if(yyr>=0 and xxr>=0):
                img1[d2-yyr-1, xxr] = img0[d2-i-1, j]

cv2.imshow(w1,img0)
cv2.imshow(w2,img1)
cv2.waitKey(0)
cv2.destroyAllWindows()