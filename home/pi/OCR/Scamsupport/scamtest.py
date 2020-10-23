import numpy as np
import cv2
pic = np.zeros((500,500,3),dtype = 'uint8')
cv2.line(pic, (200,200),(500,200),(0,255,0))
cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
