import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(dac, GPIO.OUT)
dr = 3.16

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dr):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dr:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage*255/dr)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def number_to_dac(number):
    for i in range(len(dec2bin(number))):
        if dec2bin(number)[i] == 1:
            GPIO.output(dac[i], 1)
        else:
            GPIO.output(dac[i], 0)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()