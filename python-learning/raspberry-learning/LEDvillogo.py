import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while True:
    GPIO.output(11,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(11,GPIO.LOW)
    time.sleep(1)
