import cv2
import numpy as np

img = cv2.imread('images/test.png',cv2.IMREAD_GRAYSCALE)


(d1,d2)=img.shape


r = np.zeros((256))

s=-1
l=-1

for i in range(0,d1):
    for j in range(0,d2):
        temp = img[i,j]
        r[temp]=1

for i in range(0,256):
    if(r[i]==1):
        s=l
        l=i

if(s!=-1):
    print('second largest value :',s)
else:
    print('image has a single intensity value ',l)