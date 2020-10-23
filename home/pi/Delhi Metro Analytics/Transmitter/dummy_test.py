import RPi.GPIO as GPIO
import time
import cv2
from picamera import PiCamera
import numpy as np

#Reading saved image we just captured
img = cv2.imread('peds.jpeg')

            #loading haarcascade
upper_cascade = cv2.CascadeClassifier('/home/pi/Project/Metro_Analytics/Transmiter/haarcascade_lowerbody.xml')

            #converting image to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


            #detecting the no. of people in the image
people = upper_cascade.detectMultiScale(gray, 1.1, 4)

            #outling each human detected

for(x,y,w,h) in people:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
print
            # DISPLAYING RESULT
cv2.imshow('img',img)
cv2.waitKey(0)








            #haarcascade_lowerbody.xml






            

            
           


