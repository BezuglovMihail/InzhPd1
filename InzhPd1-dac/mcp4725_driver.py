import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.adress = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range
    def deinit(self):
        self.bus.close()
    def set_number(self, number):
        if not isinstance(number, int):
            print("Na vhod CAP mozhno podavat tolko celye chisla")
        
        if not (0 <= number <= 4095):
            print("X=Chislo vyhodit za razryadnost MCP4752 (12 bit)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Chislo: {number}, otpravlennye po I2C dannye: [0x{(self.adress << 1):02X}, 0x{second_byte:02X}]\n")
    def set_voltage(self, voltage):
        number = (5 / voltage) * 4095
        self.bus.write_byte_data(0x61, [int(el) for el in bin(number)[2:].zfill(8)])
    
if __name__ == "__main__":
    try:
        dac = MCP4725(4095)
    
        while True:
            try:
                number = float(input("Na vhod CAP mozhno podavat tolko celye chisla"))
                dac.set_number(number)

            except ValueError:
                print("Poprobyite esho raz.\n")
    finally:
        dac.deinit()

        