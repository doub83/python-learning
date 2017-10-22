import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
while True:
    GPIO.output(3,GPIO.HIGH) #Piros LED ON
    time.sleep(5) #vár 5sec
    GPIO.output(5,GPIO.HIGH) #Sárga LED ON
    time.sleep(2) #vár 2sec
    GPIO.output(5,GPIO.LOW) #Sárga LED OFF
    GPIO.output(3,GPIO.LOW) #Piros LED OFF
    GPIO.output(7,GPIO.HIGH) #Zöld LED ON
    time.sleep(10) #Vár 10sec
    GPIO.output(7, GPIO.LOW) #Zöld LED OFF
    GPIO.output(5, GPIO.HIGH) #Sárga LED ON
    time.sleep(5)  # vár 5sec
    GPIO.output(5,GPIO.LOW)

