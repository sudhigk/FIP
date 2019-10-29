# bit plane slicing
import cv2
import numpy as np

img = cv2.imread("images/test.jpg",cv2.IMREAD_GRAYSCALE)

w0 = 'input'
w1 = 'one'
w2 = 'two'
w3 = 'three'
w4 = 'four'
w5 = 'five'
w6 = 'six'
w7 = 'seven'
w8 = 'eight'


cv2.namedWindow(w0,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w0,300,300)
cv2.moveWindow(w0,0,0)

cv2.namedWindow(w1,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w1,300,300)
cv2.moveWindow(w1,300,0)

cv2.namedWindow(w2,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w2,300,300)
cv2.moveWindow(w2,600,0)

cv2.namedWindow(w3,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w3,300,300)
cv2.moveWindow(w3,900,0)

cv2.namedWindow(w4,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w4,300,300)
cv2.moveWindow(w4,1200,0)

cv2.namedWindow(w5,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w5,300,300)
cv2.moveWindow(w5,300,300)

cv2.namedWindow(w6,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w6,300,300)
cv2.moveWindow(w6,600,300)

cv2.namedWindow(w7,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w7,300,300)
cv2.moveWindow(w7,900,300)

cv2.namedWindow(w8,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w8,300,300)
cv2.moveWindow(w8,1200,300)


(d1,d2) = img.shape

one = np.zeros((d1,d2,1),np.uint8)
two = np.zeros((d1,d2,1),np.uint8)
three = np.zeros((d1,d2,1),np.uint8)
four = np.zeros((d1,d2,1),np.uint8)
five = np.zeros((d1,d2,1),np.uint8)
six = np.zeros((d1,d2,1),np.uint8)
seven = np.zeros((d1,d2,1),np.uint8)
eight = np.zeros((d1,d2,1),np.uint8)


for i in range( d1):
    for j in range( d2):
        n = int(img[i,j])
        if(n != 0):
            one[i,j] = ( n % 2) * 1
            n = n / 2
        if (n != 0):
            two[i, j] = ( n % 2) * 2
            n = n / 2
        if (n != 0):
            three[i, j] = ( n % 2) * 4
            n = n / 2
        if (n != 0):
            four[i, j] = ( n % 2) * 8
            n = n / 2
        if (n != 0):
            five[i, j] = ( n % 2) * 16
            n = n / 2
        if (n != 0):
            six[i, j] = ( n % 2) * 32
            n = n / 2
        if (n != 0):
            seven[i, j] = ( n % 2) * 64
            n = n / 2
        if (n != 0):
            eight[i, j] = ( n % 2) * 128
            n = n / 2

cv2.imshow(w0,img)
cv2.imshow(w1,one)
cv2.imshow(w2,two)
cv2.imshow(w3,three)
cv2.imshow(w4,four)
cv2.imshow(w5,five)
cv2.imshow(w6,six)
cv2.imshow(w7,seven)
cv2.imshow(w8,eight)
cv2.waitKey(0)
cv2.destroyAllWindows()