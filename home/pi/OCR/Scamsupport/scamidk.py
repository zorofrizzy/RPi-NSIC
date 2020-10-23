import numpy as np
import cv2
pic = cv2.imread('clipp.jpg')
gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
blurImg = cv2.blur(gray,(40,40))
result = blurImg-gray
cv2.imshow('resultant',result)



#xy = cv2.bitwise_not(result)
cv2.imwrite('whoa.jpg', result)

#cv2.imshow('resultant inv',xy)

#cv2.imwrite('xy.jpg', xy)
cv2.waitKey(0)
cv2.destroyAllWindows()
