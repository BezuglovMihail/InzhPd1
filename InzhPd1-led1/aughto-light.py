import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
ftr = 6
GPIO.setup(ftr, GPIO.IN)
while True:
    if not GPIO.input(ftr):
        GPIO.output(led, True)
        time.sleep(0.2)
        GPIO.output(led, False)