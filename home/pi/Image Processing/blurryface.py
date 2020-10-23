import cv2
import numpy as np


cons = cv2.imread("nightwing.jpeg")
cv2.imshow("Constantine", cons)


kernel = np.ones((11,11), np.float32)/121
averaged = cv2.filter2D(cons, -1, kernel)
cv2.imshow("avg", averaged)

blurredA = cv2.blur(cons, (11,11))
cv2.imshow("AvgBlur", blurredA)


blurredG = cv2.GaussianBlur(cons, (11,11), 0)
cv2.imshow("GBlur", blurredG)


blurredM = cv2.medianBlur(cons, 5)
cv2.imshow("MBlur", blurredM)

blurredB = cv2.bilateralFilter(cons, 9, 75, 75)
cv2.imshow("BBlur", blurredB)


cv2.waitKey(0)
