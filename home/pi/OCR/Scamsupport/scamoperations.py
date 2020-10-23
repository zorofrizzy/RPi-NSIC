import cv2
import numpy as np
pic = cv2.imread('avengers.jpg')
#original
cv2.imshow('pic',pic)
#bilateral
dimpixel = 7
color = 100
space = 100
filter = cv2.bilateralFilter(pic,dimpixel,color,space)
cv2.imshow('bilateralfilter',filter)
#erosion
pict = cv2.imread('avengers.jpg',0)
kernel = np.ones((4,4),np.uint8)
erosion = cv2.erode(pict,kernel,iterations = 1)
cv2.imshow('erosion', erosion)
#dilation
dilation = cv2.dilate(pict,kernel,iterations = 1)
cv2.imshow('dilation',dilation)
#opening
opening = cv2.morphologyEx(pict,cv2.MORPH_OPEN,kernel)
cv2.imshow('opening',opening)
#closing
closing = cv2.morphologyEx(pict,cv2.MORPH_CLOSE,kernel)
cv2.imshow('closing',closing)
#gradient
gradient = cv2.morphologyEx(pict,cv2.MORPH_GRADIENT,kernel)
cv2.imshow('gradient',gradient)
#tophat
tophat= cv2.morphologyEx(pict,cv2.MORPH_TOPHAT,kernel)
cv2.imshow('tophat',tophat)
#blackhat
blackhat = cv2.morphologyEx(pict,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('blackhat',blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
