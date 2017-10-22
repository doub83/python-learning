import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p=GPIO.PWM(12, 50)
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            print(dc)
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            print(dc)
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
        pass
p.stop()
input("Leállításhoz nyomj egy ENTER - t")
p.stop()
GPIO.cleanup() //vege
