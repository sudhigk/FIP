# rough works
import numpy as np
import cv2
# Read the image in greyscale
img = cv2.imread('images/test.jpg',0)

#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j] ,width=8)) # width = no. of bits
print(type(lst[0]))