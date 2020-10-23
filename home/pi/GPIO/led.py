import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) #SET AS OUTPUT
while True:
    GPIO.output(17, GPIO.LOW)
   # time.sleep(2)
    #GPIO.output(17, GPIO.HIGH)
    time.sleep(2)


