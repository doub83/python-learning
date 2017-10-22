import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p=GPIO.PWM(12, 0.5) #PWM üzemmód behívása a GPIO 12 - es tüskéjére a frekvencia 0,5HZ
p.start(1) #Indítás
input("Leállításhoz nyomj egy ENTER - t")
p.stop()
GPIO.cleanup()

