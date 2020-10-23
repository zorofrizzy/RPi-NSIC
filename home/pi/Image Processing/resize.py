import cv2
import numpy

#resize

ball = cv2.imread("pokeball.jpg")


resizedball = cv2.resize(ball, None, fx=4, fy=3, interpolation = cv2.INTER_CUBIC)

cv2.imshow("RESIZED", resizedball)

cv2.waitKey(0)


    
