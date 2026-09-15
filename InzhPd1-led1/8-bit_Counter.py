import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
leds.reverse()
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
GPIO.setup([9, 10], GPIO.IN)
num = 0
def dec2bin (v):
    return [int(el) for el in bin(v)[2:].zfill(8)]
sleep_time = 0.2
while True:
    if GPIO.input(9):
        num += 1
        print (num, dec2bin(num))
        if num == 256:
            num = 0
        GPIO.output(leds, dec2bin(num))
    time.sleep(sleep_time)
    if GPIO.input(10):
        num -= 1
        if num == -1:
            num = 255
        print (num, dec2bin(num))
        GPIO.output(leds, dec2bin(num))



    time.sleep(sleep_time)