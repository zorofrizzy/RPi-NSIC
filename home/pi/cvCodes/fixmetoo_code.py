import numpy
import cv2

ama=cv2.imread("red.jpg")
cv2.imshow("outputWindow", ama)

row1=ama.shape[0]
col1=ama.shape[1]

pixel=row1*col1


row=0
col=0
while row<=row1:
    while col<=col1:
        
        b=ama[row,col,0]
        g=ama[row,col,1]
        r=ama[row,col,2]

        col=col+1
        
    row=row+1

x=0

while x<=row1:
    b[




