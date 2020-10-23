import cv2
import numpy

ama=cv2.imread("3.jpg")
cv2.imshow("outputWindow", ama)

grayConverted = cv2.cvtColor(ama, cv2.COLOR_BGR2GRAY)
cv2.imshow("convertedGray", grayConverted)

binary = cv2.threshold(grayConverted, 150,255, cv2.THRESH_BINARY)[1]
cv2.imshow("convertedBW", binary)

booster_gold = ama[20:500,10:800] #crop the image, starting at this pixel to this pixel. [columns:rows]
cv2.imshow("segmented image", booster_gold)

booster_gold1 = ama[10:340,10:535] #crop the image, starting at this pixel to this pixel. [columns:rows]
cv2.imshow("segmented image2", booster_gold1)

keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
    cv2.waitKey(1)
