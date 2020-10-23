import cv2
import numpy

batman = cv2.imread("batcrop.jpg")
fence = cv2.imread("batfinal.jpg")
batman = batman[0:625,0:1000]
fence = fence[0:625,450:1450]

cv2.imshow("Batman", batman)
cv2.imshow("Fence", fence)

#batbar = cv2.addWeighted(batman, 0.4, fence, 1, 0.5)
batbar = cv2.add(batman, fence)


"""
myfont=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(batbar, "he's back!", (450,450), myfont, 1, [150,150,150], 2)

"""

cv2.imshow("BAT BAR", batbar)


#cv2.imwrite("Bat_Bar.jpg", batbar)

cv2.waitKey(0)


