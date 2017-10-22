import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, 0)

while True:
    gomb = GPIO.input(7)
    if gomb==1:
        print("Kapcsoló bent")
        GPIO.output(11,1)
    else:
        GPIO.output(11, 0)

    time.sleep(0.5)
