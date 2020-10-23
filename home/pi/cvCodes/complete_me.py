import numpy
import cv2

ama=cv2.imread("red.jpg")
cv2.imshow("outputWindow", ama)

row1=ama.shape[0]
col1=ama.shape[1]

pixel=row1*col1

mask_red = cv2.inRange(image_input, np.array([0,0,10]), np.array([80,80,355]
