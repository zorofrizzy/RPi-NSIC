import numpy as np
import cv2
pic = np.zeros((500,500,3),dtype = 'uint8')
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, 'Zorawar Nibba never stops',(100,100),font,0.5,(255,0,0),1,cv2.LINE_8)
cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
