import cv2
import numpy

#resize

ball = cv2.imread("droopy.jpg")


#RESIZE THE IMAGE

resizedball = cv2.resize(ball, None, fx=3, fy=2, interpolation = cv2.INTER_CUBIC)
"""
cv2.imshow("RESIZED", resizedball)
"""
#FONT

myFont = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(resizedball, "ALSO I'M BATMAN", (200,550), myFont, 2, [0,0,0], 3)
cv2.imshow("RESIZED WITH TEXT", resizedball)


cv2.waitKey(0)


    
