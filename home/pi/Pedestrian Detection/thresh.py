#adaptive threshold

#from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time

camera = PiCamera()
camera.resolution=(100,100)

camera.start_preview()
time.sleep(4)
camera.capture('pic023.jpg')
time.sleep(1)
camera.stop_preview()

"""image = cv2.imread("pic01.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("ADAPTIVE", adaptive)
"""
keypressed = cv2.waitKey(0)

if keypressed==27:
    cv2.destroyAllWindows()

