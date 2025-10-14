import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 1
signal_frequency = 1
sampling_frequency = 10

if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 1000, 3.14, True)

        while True:
            dac.set_voltage(amplitude*sg.get_sin_wave_amplitude(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()