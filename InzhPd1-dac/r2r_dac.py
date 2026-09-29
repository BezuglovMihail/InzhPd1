import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup(self.gpio_bits, 0)
    def num_to_dac (numb):
        GPIO.output (self.gpio_bits, 0)
        GPIO.output(self.gpio_bits, [int(el) for el in bin(numb)[2:].zfill(8)])
    def voltage_to_number(voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Зн. не входит в допустимый диап. для ЦАП (до {self.dynamic_range:.2f} B)")
            print("Установим напряжение 0.0 В")
            return 0
        
        return int(voltage / self.dynamic_range * 255)


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25,26,17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Vvedite napryazhenie v Voltah: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Vy vveli ne chislo. Poprobyite escho raz\n")
    finally:
        dac.deinit()

