import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
phtr = 6
GPIO.setup(phtr, GPIO.IN)
while True:
    state = GPIO.input(phtr)
    state = not state
    GPIO.output(led, state)
