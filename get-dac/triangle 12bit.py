import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.15
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        mcp = mcp.MCP4725(5.15, True)

        while True:
            mcp.set_voltage(amplitude*sg.get_triangle(signal_frequency, time.time()))
            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        mcp.deinit()