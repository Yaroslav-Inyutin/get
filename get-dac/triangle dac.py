import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.15
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        pwm = pwm.PWM_DAC(12, 500, 3.16, True)

        while True:
            pwm.set_voltage(amplitude*sg.get_triangle(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        pwm.deinit()