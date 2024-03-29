# convolution in simple matrix
import cv2
import numpy as np
# img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
# (d1,d2) = img1.shape
# print(d1,d2)

img1 = np.zeros((3,3,3), np.uint8)
d1 = 3
d2 = 3
nm = 1
for i in range(0,d1):
    for j in range(0,d2):
        img1[i,j,0] = nm
        img1[i, j, 1] = nm
        img1[i, j, 2] = nm
        nm = nm +1

md1 = 3
md2 = 3
# mask = np.zeros((md1,md2,3), np.uint8)
# mask =np.array([[0.0,0.0],[0.0,0.0],[0.0,0.0]])
mask =np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
for i in range(0,md1):
    for j in range(0,md2):
        mask[i,j] = 1/9

nd1 = d1+md1-1
nd2 = d2+md2-1

otpt = np.zeros((nd1,nd2,3), np.uint8)



w1 = 'input'
w2 = 'output'

cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

for i in range(0,md1):
    for j in range(0,md2):
        print("hi ",mask[i,j])
print("\nresult without rounding\n")

for i in range(0,nd1):
    for j in range(0,nd2):
        s = 0
        print("value of y(",i,",",j,")= ",end='')
        for m in range(0,md1):
            if((i-m)>=0 and (i-m)<d1):
                for n in range(0,md2):
                    if((j-n)>=0 and (j-n)<d2):
                        # print(m, n)
                        # s = float(s) + float(mask[m, n]) * float(img1[i - m, j - n])
                        s = s + mask[m, n] * img1[i-m, j-n]
                        print(" + (","%.2f"%mask[m,n],"*","%.2f"%img1[i-m, j-n,0],end=' )')
        # print(type(s))
        otpt[i,j] = s
        print(" = %.2f"%s[0])
    print('\n')
print("\nrounder result\n")
for i in range(0,nd1):
    print("\n")
    for j in range(0,nd2):
        print(otpt[i,j,0]," ")