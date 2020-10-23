import numpy as np
import cv2
pic = np.zeros((500,500,3),dtype = 'uint8')
cv2.rectangle(pic, (20,20),(500,150),(0,255,0), 10 , lineType=2,shift=0)
cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
