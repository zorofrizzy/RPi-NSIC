import numpy
import cv2

droopy = cv2.imread("droopy.jpg")
cv2.imshow("original", droopy)
resized= cv2.resize(droopy, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)


translationMatrix = numpy.float32([[1,0,60],[0,1,30]])
translated = cv2.warpAffine(resized, translationMatrix, (resized.shape[1], resized.shape[0]))
cv2.imshow("TRANSLATION", translated)


rotationMatrix = cv2.getRotationMatrix2D((resized.shape[1]/2, resized.shape[0]/2), 90, 1)
rotated = cv2.warpAffine(resized, rotationMatrix, (resized.shape[0], resized.shape[1]))
cv2.imshow("ROTATED", rotated)

cv2.waitKey(0)
