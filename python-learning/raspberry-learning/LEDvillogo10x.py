import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
print ("LED villog 10-szer")
GPIO.setmode (GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
for i in range(1, 11, 1):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.250)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.250)

