import numpy as np
import time
import math

def get_sin_wave_amplitude(freq, time):
    return (np.sin(2*np.pi*freq*time)+1)/2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(float(1/sampling_frequency))

def get_triangle(freq, time):
    return 2*abs(freq*time - math.floor(freq*time) - 0.5)
    