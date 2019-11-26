import cv2
import numpy as np

img = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)


(d1,d2)=img.shape


r = np.zeros((256))

s=-1
l=-1

for i in range(0,d1):
    for j in range(0,d2):
        temp = img[i,j]
        r[temp]=r[temp]+1

for i in range(0,256):
    if(r[i]!=0):
        s=l
        l=i

# for i in range(0,256):
#     print(i,r[i])

if(s!=-1):
    print('second largest intensity :',s,'\tcount:',r[s])
else:
    print('image has a single intensity value ',l,'count:',l)