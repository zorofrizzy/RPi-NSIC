import RPi.GPIO as GPIO
import time
import cv2
from picamera import PiCamera
import numpy as np

"""
GPIO.setmode(GPIO.BOARD)

#DEFINING 3 GPIOS FOR IR SENSORS

GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)           


if (GPIO.input(7)):
    if (GPIO.input(8)):
        if (GPIO.input(10)):
            #ALL 3 IR SENSORS ARE HIGH. THIS MEANS THAT THE TRAIN IS IN BETWEEN TWO STATIONS, WE NOW CLICK A PICTURE.
            camera = PiCamera()
            camera.resolution = (1024, 768)
            camera.start_preview()

            time.sleep(2)

            camera.capture('nspL.jpg')
            # IMAGE HAS BEEN CLICKED NOW WE PROCESS IT USING HAARCASCADES TO FIND THE NO. OF PEOPLE.
            time.sleep(2)
            camera.close_preview()

            # NOW WE PROCESS THE IMAGE
"""
            #Reading saved image we just captured
img = cv2.imread('peds.jpg')

            #loading haarcascade
upper_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

            #converting image to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


            #detecting the no. of people in the image
people = upper_cascade.detectMultiScale(gray, 1.1, 4)

            #outling each human detected

for(x,y,w,h) in people:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

            # DISPLAYING RESULT
cv2.imshow('img',img)
cv2.waitKey(0)




#GPIO.cleanup()
            

            
           


