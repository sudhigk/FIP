# rough works
import numpy as np
import cv2
# Read the image in greyscale
img1 = cv2.imread('images/test.jpg',0)

s = [0] * 9

s = [int(0)] * 9
for m in range(0,3):
    for n in range(0,3):
        s[( m * 3) + n] =(img1[1000-3-1+m, 100-3-1+n])
        print((img1[1000-3-1+m, 100-3-1+n]))
print(s)
s.sort()
otpt = s[4]

print(s)


print(otpt)