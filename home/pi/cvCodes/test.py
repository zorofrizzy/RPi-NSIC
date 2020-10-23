import numpy
import cv2

testimage=cv2.imread("2.jpg")
cv2.imshow("OutputW1",testimage)

segment = testimage[200:1270,100:1500]
segmentgray=cv2.cvtColor(segment, cv2.COLOR_BGR2RGB)
testimage[200:1270,100:1500] = segmentgray[0:segmentgray.shape[0],0:segmentgray.shape[1]]

                         
                         


#//converts the omage to grey colour
cv2.imshow("OutputW",testimage)

keypressed = cv2.waitKey()
if keypressed == 27:
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
