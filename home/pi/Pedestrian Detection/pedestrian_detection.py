from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
"""
camera = PiCamera()
camera.resolution = (240,320)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size = (240,180))
"""
display_window = cv2.namedWindow("CAPTURE")
wid = 0
num = 0
face_cascade = cv2.CascadeClassifier('/home/pi/Cascades/opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml')

time.sleep(1)

for frame in camera.capture_continuous(rawCapture, format = "bgr", use_video_port = True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectionMultiScale(gray, 1.1, 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, str(num), (200,40), font, 1, (255,255,255),1)

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, x+y), (0,255,0), 2)
        if(w>wid):
            num = num+1
            print "OUT " + "TOTAL : " + str(num)
        else:
            num = num-1
            print "OUT "+ "TOTAL :" +str(num)
        wid = w
    cv2.imshow("CAPTURE", image)
    key = cv2.waitKey(1)

    rawCapture.truncate(0)

    if key==27:
        camera.close()
        cv2.destroyAllWindows()
        break
