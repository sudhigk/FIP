# smoothing by weighted averaging filter
import cv2
import numpy as np
img1 = cv2.imread('images/test.jpg',cv2.IMREAD_GRAYSCALE)
(d1,d2) = img1.shape
print(d1,d2)


md1 = 3
md2 = 3

# mask = np.zeros((md1,md2,3), np.uint8)



nd1 = d1+md1-1
nd2 = d2+md2-1

otpt = np.zeros((nd1,nd2,3), np.uint8)



w1 = 'input'
w2 = 'output'

cv2.namedWindow(w1,cv2.WINDOW_NORMAL)
cv2.resizeWindow(w1,400,400)
cv2.moveWindow(w1,0,0)

cv2.namedWindow(w2,cv2.WINDOW_NORMAL)
cv2.resizeWindow(w2,400,400)
cv2.moveWindow(w2,0,400)

ch = int(input("SMOOTHING\n1.average\n2.median\n3.gaussian\n:"))

if(ch==1):

    mask = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

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
                            s =float(s) + float(mask[m, n]) * float(img1[i-m, j-n])

            otpt[i,j] = int((1/16) * s )

    # for i in range(0,nd1):
    #     print("\n")
    #     for j in range(0,nd2):
    #         print(otpt[i,j,0]," ")

elif(ch==2):
# ------------------------MEDIAN-----------------------
    mask =np.array([[1,1,1],[1,1,1],[1,1,1]])

    for i in range(0,md1):
        for j in range(0,md2):
            print(mask[i,j])

    s = [0] * 9

    for i in range(0,nd1):
        for j in range(0,nd2):
            s = [int(0)] * 9
            for m in range(0,md1):
                if((i-m)>=0 and (i-m)<d1):
                    for n in range(0,md2):
                        if((j-n)>=0 and (j-n)<d2):
                            # print(m, n)
                            s[( m * 3) + n] = (mask[m, n]) * (img1[i-m, j-n])
            s.sort()
            otpt[i,j] = s[4]
#----------------------MEDIAN END----------------------
elif(ch==3):
    mask2 = np.array([[0.3679, 0.6065, 0.3679], [0.6065, 1.0000, 0.6065], [0.3679, 0.6065, 0.3679]])

    for i in range(0, nd1):
        for j in range(0, nd2):
            s = 0.0
            for m in range(0, md1):
                if ((i - m) >= 0 and (i - m) < d1):
                    for n in range(0, md2):
                        if ((j - n) >= 0 and (j - n) < d2):
                            # print(m, n)
                            s = float(s) + float(mask2[m, n]) * float(img1[i - m, j - n])
            s = s/4.8976
            otpt[i, j] = int(s)

cv2.imwrite("images/output.jpg",otpt)
cv2.imshow(w1,img1)
cv2.imshow(w2,otpt)
cv2.waitKey(0)
cv2.destroyAllWindows()