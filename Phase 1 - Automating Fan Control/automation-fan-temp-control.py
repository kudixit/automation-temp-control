import os
import glob
import time
import RPi.GPIO as GPIO

# === GPIO Setup ===
RELAY_PIN = 17  # GPIO17 = physical pin 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# === DS18B20 Sensor Setup ===
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]  # Get first '28-' folder
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as f:
        return f.readlines()

def read_temp():
    lines = read_temp_raw()
    
    # Wait until the first line ends with 'YES' (valid data)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    # Parse temperature value from second line
    temp_pos = lines[1].find('t=')
    if temp_pos != -1:
        temp_string = lines[1][temp_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    return None

# === Main Loop ===
try:
    while True:
        temp = read_temp()
        print(f"Temperature: {temp:.2f}°C")

        # Control logic: Fan ON at 30°C, OFF at 28°C (hysteresis)
        if temp >= 28.0:
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Relay ON → Fan ON
            print("Fan ON")
        elif temp <= 27.0:
            GPIO.output(RELAY_PIN, GPIO.LOW)   # Relay OFF → Fan OFF
            print("Fan OFF")

        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    GPIO.cleanup()