import cv2
print(cv2.__version__)

image1 = cv2.imread('images/test.png',cv2.IMREAD_GRAYSCALE)

#image0 = cv2.imread('images/dots.png')
image0 = cv2.imread('images/test.png')
#image0 = cv2.imread('images/yodha.jpg')

#cv2.imshow('sudhi',image)

firstwindow = "imput image"
secondwindow = "output image"

cv2.namedWindow(firstwindow,cv2.WINDOW_NORMAL)
cv2.resizeWindow(firstwindow,400,400)
cv2.moveWindow(firstwindow,50,0)

cv2.namedWindow(secondwindow,cv2.WINDOW_NORMAL)
cv2.resizeWindow(secondwindow,400,400)
cv2.moveWindow(secondwindow,100,400)

#px = image1[25,25]
#print(px)
(dim1,dim2, dim3) = image0.shape
print('rows =',dim1)
print('columns =',dim2)
print('d3',dim3)
print(image0[0,20])

for i in range (0,dim1):

        for j in range (0,dim2):

            if(image1[i,j]>180 and image1[i, j]<245 ):
             image0[i, j] = [255, 0, 0]
             #print(i,' ',j,' high intensity')
             #image0[i, j] = image1[i, j] - (10, 10, 10)
            elif(image1[i,j]<90 ):
             image0[i, j] = [0, 0, 255]
             #print(i,' ', j,' medium intensity')
            elif (image1[i, j]<245):
             image0[i, j] = [0, 255, 0]
             #print(i, ' ', j, ' low intensity')


cv2.imshow(firstwindow,image1)
cv2.imshow(secondwindow,image0)

cv2.waitKey(0)
cv2.destroyAllWindows()