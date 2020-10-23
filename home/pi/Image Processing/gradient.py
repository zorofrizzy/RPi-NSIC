
import cv2
import numpy

droopy = cv2.imread("grad.jpeg")
cv2.imshow("ORIGINAL", droopy)


robingray = cv2.cvtColor(droopy, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", robingray)

#TRUNK - SAY THE VALUE IS SET TO 63, THEN THE GRADIENT CHANGES GRADUALLY UPTO 63, THEREAFTER ITS CONSTANT, SET TO 63
thresh1 = cv2.threshold(robingray, 127, 255, cv2.THRESH_BINARY)[1]
thresh2 = cv2.threshold(robingray, 127, 255, cv2.THRESH_BINARY_INV)[1]
thresh3 = cv2.threshold(robingray, 127, 255, cv2.THRESH_TOZERO)[1]
thresh4 = cv2.threshold(robingray, 127, 255, cv2.THRESH_TOZERO_INV)[1]
thresh5 = cv2.threshold(robingray, 127, 255, cv2.THRESH_TRUNC)[1]
thresh6 = cv2.adaptiveThreshold(robingray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh7 = cv2.adaptiveThreshold(robingray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow("thresh1", thresh1)
cv2.imshow("thresh2", thresh2)
cv2.imshow("thresh3", thresh3)
cv2.imshow("thresh4", thresh4)
cv2.imshow("thresh5", thresh5)
cv2.imshow("thresh6", thresh6)
cv2.imshow("thresh7", thresh7)

cv2.waitKey(0)

#ADAPTIVE CALCULATES THE THRESHOLD AUTOMATICALLY AND ADJUSTS THE SAME AS PER THE IMAGE, THUS THE IMAGE IS NOT LOST.
