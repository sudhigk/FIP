# histogram equalization
import cv2
import numpy as np
# img0 = cv2.imread('images/histo.png',cv2.IMREAD_GRAYSCALE)
img0 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)


(d1, d2) = img0.shape
print(d1,d2)
otpt = np.zeros((d1,d2,1), np.uint8)



r = np.zeros(256)
p = np.zeros(256)
s = np.zeros(256)

w1 = 'input'
w2 = 'output'

cv2.namedWindow(w1,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_KEEPRATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

print(type(d1))


def contr(p,li,hi,lo,ho):
    return( ( (p-li) * (ho-lo) / (hi-li) ) + lo )

for i in range (0, 101):
    r[i] = contr(i,0,100,0,55)

for i in range (101, 156):
    r[i] = contr(i,100,155,55,200)

for i in range (156, 256):
    r[i] = contr(i,155,255,200,255)

for i in range (0, d1):
    for j in range (0, d2):
        temp = img0[i,j]
        otpt[i,j]= r[temp]



print(type(i))
cv2.imshow(w1,img0)
cv2.imshow(w2,otpt)
cv2.waitKey(0)
cv2.destroyAllWindows()