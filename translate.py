# image translation
import cv2
img0 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)

(d2, d1) = img0.shape
print(d1,d2)

w1 = 'input'
w2 = 'output'
cv2.namedWindow(w1,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_FREERATIO)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

print(type(d1))

dx = int(input('enter the shift value of x:'))
dy = int(input('enter the shift value of y:'))


for i in range (0 ,d2):
    for j in range (0, d1):
        img1[i,j] = 0

for i in range (0, d2):
    ty= i-dy
    for j in range(0, d1):
        tx= j+dx
        if(ty<d2 and tx<d1):
            if(ty>=0 and tx>=0):
                img1[ty, tx]= img0[i,j]

cv2.imshow(w1,img0)
cv2.imshow(w2,img1)
cv2.waitKey(5000)
cv2.destroyAllWindows()