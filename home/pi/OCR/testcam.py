from time import sleep
from picamera import PiCamera
import cv2
import numpy

"""
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('testimage.jpg')
camera.stop_preview()
"""
                                                                                                                 
ama=cv2.imread("testimage.jpg")
grayConverted = cv2.cvtColor(ama, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(grayConverted, 200,255, cv2.THRESH_BINARY)[1]
img_not = cv2.bitwise_not(binary)
cv2.imwrite("testconv.jpg", img_not)
