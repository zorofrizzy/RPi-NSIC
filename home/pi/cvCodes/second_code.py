import cv2
import numpy

ama=cv2.imread("2.jpg")
cv2.imshow("OutputW1",ama)

ama=cv2.imread("2.jpg",0)    //converts the omage to grey colour
cv2.imshow("OutputW",ama)

keypressed = cv2.waitKey()
if keypressed == 27:
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
