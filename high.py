import cv2
print(cv2.__version__)

image1 = cv2.imread('images/sudhi.jpg',cv2.IMREAD_GRAYSCALE)


(dim1,dim2) = image1.shape
print('rows =',dim1)
print('columns =',dim2)
# print('d3',dim3)
print(image1[0,20])
s = 0
print(s)
for i in range (0,dim1):

        for j in range (0,dim2):

            if(image1[i,j]>s ):
                s = image1[i,j]
                print(s)

print("high :",s)

cv2.waitKey(0)
cv2.destroyAllWindows()