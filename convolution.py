# convolution using mask
import cv2
import numpy as np
img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
(d1,d2) = img1.shape
print(d1,d2)

# img1 = np.zeros((2,3,3), np.uint8)
# d1 = 2
# d2 = 3
# nm = 4
# for i in range(0,2):
#     for j in range(0,3):
#         img1[i,j,0] = nm
#         img1[i, j, 1] = nm
#         img1[i, j, 2] = nm
#         nm = nm +1

md1 = 3
md2 = 3

# mask = np.zeros((md1,md2,3), np.uint8)
mask =np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
for i in range(0,md1):
    for j in range(0,md2):
        mask[i,j] = 1/9

nd1 = d1+md2-1
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
        print(mask[i,j])

for i in range(0,nd1):
    for j in range(0,nd2):
        s = 0.0
        for m in range(0,md1):
            if((i-m)>=0 and (i-m)<d1):
                for n in range(0,md2):
                    if((j-n)>=0 and (j-n)<d2):
                        # print(m, n)
                        s = float(s) + float(mask[m, n]) * float(img1[i-m, j-n])
        otpt[i,j] = int(s)

# for i in range(0,nd1):
#     print("\n")
#     for j in range(0,nd2):
#         print(otpt[i,j,0]," ")

cv2.imshow(w1,img1)
cv2.imshow(w2,otpt)
cv2.waitKey(0)
cv2.destroyAllWindows()