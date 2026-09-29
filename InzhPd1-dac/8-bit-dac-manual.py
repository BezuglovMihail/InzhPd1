import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
leds = [22, 27, 17, 26, 25, 21, 20, 16]
2
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

dynRg = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynRg):
        print(f"Зн. не входит в допустимый диап. для ЦАП (до {dynRg:.2f} B)")
        print("Установим напряжение 0.0 В")
        return 0
    
    return int(voltage / dynRg * 255)

def num_to_dac (numb):
    GPIO.output (leds, 0)
    GPIO.output(leds, [int(el) for el in bin(numb)[2:].zfill(8)])

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            numb = voltage_to_number(voltage)
            num_to_dac(numb)
        except ValueError:
            print("Вы ввели не число. Повторите ввод\n")
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()