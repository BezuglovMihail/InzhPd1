import RPi.GPIO as GPIO
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        GPIO.setmode(GPIO.BCM)
        led = gpio_pin
        GPIO.setup(led, GPIO.OUT, initial=0)
        pwm = GPIO.PWM(led, pwm_frequency)
        duty = 0.0
        pwm.start(duty)
        while True:
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.05)

            duty += 1.0
            if duty > 100.0:
                duty = 0.0
    def deinit(self):
        GPIO.output (self.led, 0)
        GPIO.cleanup()
    def set_voltage(self, voltage):
        duty = int(voltage / self.dynamic_range * 255) % 256
        self.set_number(duty)
    
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
    
        while True:
            try:
                voltage = float(input("Vvedite napryazhenie v Voltah: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Vy vveli ne chislo, poprobyite esho raz.\n")
    finally:
        dac.deinit()
