import cv2
import numpy

ama=cv2.imread("2.jpg")
cv2.imshow("outputWindow", ama)

grayConverted = cv2.cvtColor(ama, cv2.COLOR_BGR2GRAY)
cv2.imshow("convertedGray", grayConverted)


binary = cv2.threshold(grayConverted, 150,255, cv2.THRESH_BINARY)[1]
cv2.imshow("convertedBW", binary)

#cv2.imwrite("BandW.jpg",binary)

#imwrite saved the image....

booster_gold = ama[10:340,10:535] #crop the image, starting at this pixel to this pixel. [columns:rows]
cv2.imshow("segmented image", booster_gold)

keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
    cv2.waitKey(1)
