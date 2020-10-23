"""pasting a part of the image on top of the other"""
import cv2
import numpy

ama=cv2.imread("2.jpg")
cv2.imshow("ou", ama)

#pic displayed.
#cropping now.

crop1 = ama[20:340,10:535]

rowSize=ama.shape[0]
colSize=ama.shape[1]

rowSize1=crop1.shape[0]
colSize1=crop1.shape[1]

ama[rowSize-rowSize1-10:rowSize-10,colSize-colSize1-10:colSize-10] = crop1
#pasting an image on top
ama[20:340,10:535] = [255,100,255]

#cv2.imwrite("crop1.jpg",crop1)

cv2.imshow("op", ama)




keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
    cv2.waitKey(1)
