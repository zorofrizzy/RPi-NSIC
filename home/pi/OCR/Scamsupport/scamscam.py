import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('/home/pi/Cascades/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')


image = cv2.imread('avengers.jpg')
gray = image
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5)


for (x,y,w,h) in faces:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)



cv2.imshow('face' , gray)
print("Number of faces found{}".format(len(faces)))

cv2.imwrite('final.jpg', gray)
cv2.waitKey(1)

