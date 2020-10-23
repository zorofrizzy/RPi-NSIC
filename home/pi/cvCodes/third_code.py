import cv2
import numpy

ama=cv2.imread("2.jpg")
cv2.imshow("OutputW1",ama)

picgrey=cv2.imread("3.jpg",0)

#converts the omage to grey colour

#cv2.imshow("OutputW",ama)

greyconverted = cv2.cvtColor(ama, cv2.COLOR_BGR2HSV) #converts the image to hsv, do the same for gray
#cv2.imshow("hsv image",greyconverted)


"""ama=cv2.imread("4.jpg")
cv2.imshow("OutputW1",ama)
aman = cv2.cvtColor(ama, cv2.COLOR_BGR2LUV)
"""
devil = cv2.threshold(picgrey, 100, 255, cv2.THRESH_BINARY)[1]
#cv2.imshow("hsv image2",aman)
cv2.imshow("hsv image3",devil)

keypressed = cv2.waitKey()
if keypressed == 27:
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
