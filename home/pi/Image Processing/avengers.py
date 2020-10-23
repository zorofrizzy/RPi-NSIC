import cv2
import numpy

avengers = cv2.imread("avengers.jpg")
avenger = avengers[300:1080,:]

cv2.imshow("AVENGERS", avenger)



bordercap = cv2.copyMakeBorder(avenger, 100,100,100,100, cv2.BORDER_REFLECT)
cv2.imshow("BORDER AVENGERS", bordercap)





cv2.waitKey(0)
