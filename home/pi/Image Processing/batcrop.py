import cv2
import numpy

batman = cv2.imread("batman.jpg")
batman = batman[:,700:]

cv2.imshow("BAT CROP", batman)

cv2.imwrite("batcrop.jpg", batman)

cv2.waitKey(0)
