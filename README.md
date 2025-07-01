## Project Summary — Home Automation Temperature & Fan Control

### Phase 1: Basic Temperature Reading Setup
- Connected and configured a **DS18B20 temperature sensor** to Raspberry Pi GPIO.
- Developed Python code to **read temperature data every 2 seconds** from the sensor.
- Learned to access sensor data from `/sys/bus/w1/devices/` and parse temperature values.

### Phase 2: Data Logging & Visualization
- Built a **Dash web dashboard** to visualize live temperature data.
- Implemented CSV logging to save temperature readings with timestamps.
- Created a live updating UI with graphical temperature plots and current readings.
- Managed Python dependencies using virtual environments (`venv`).
- Resolved package compatibility issues by configuring the venv to access system-wide packages.

### Fan & Relay Control Integration
- Wired and tested a **relay module** to control a fan via Raspberry Pi GPIO pins.
- Developed Python scripts using `RPi.GPIO` to toggle the fan on/off.
- Learned hardware wiring for relay control, including power supply and grounding considerations.
- Integrated relay control and Dash UI in the same Python environment.

### Combining Software and Hardware
- Fixed compatibility issues related to Python packages (`typing_extensions`) to run Dash and hardware control simultaneously.
- Successfully ran fan control and dashboard code in a single virtual environment.
- Gained experience working inside and outside Python virtual environments to balance hardware access and package management.

---

This project provides hands-on experience in embedded programming, sensor data acquisition, data visualization, and hardware automation.

~# 🧠 Temperature-Based Fan Control using Raspberry Pi

This project is a beginner-to-intermediate home automation setup that uses 
a **Raspberry Pi**, **DS18B20 temperature sensor**, and a 
**relay-controlled fan**. The system reads live temperature data and turns 
the fan on or off based on threshold logic.

---

## 🚀 Features

- 🔄 Reads temperature every 2 seconds from a DS18B20 sensor
- ⚙️ Controls a fan via relay when temperature exceeds a threshold
- 💻 Written in pure Python, runs on Raspberry Pi
- 🔌 Simple GPIO wiring — no external microcontroller needed

---

## 🛠 Hardware Used

- Raspberry Pi (any model with GPIO)
- DS18B20 temperature sensor
- Relay module (1-channel)
- 5V Fan (low power)
- Jumper wires & breadboard
- 4.7kΩ pull-up resistor (for sensor data line)

---

## 📐 Wiring Diagram (Text Overview)

| Component         | Pi GPIO Pin        |
|------------------|--------------------|
| DS18B20 VCC      | 3.3V (pin 1)       |
| DS18B20 GND      | GND (pin 6)        |
| DS18B20 DATA     | GPIO4 (pin 7)      |
| Relay IN         | GPIO17 (pin 11)    |
| Relay DC+        | 5V (pin 2)         |
| Relay DC-        | GND (pin 6)        |
| Fan + (VCC)      | Relay NO           |
| Fan - (GND)      | GND or shared PSU  |

---

## 🧪 How It Works

1. The DS18B20 sensor is read via the Raspberry Pi’s 1-Wire interface.
2. Python checks the temperature every 2 seconds.
3. If the temperature is ≥ 30°C, the relay turns ON, activating the fan.
4. If the temperature drops to ≤ 28°C, the relay turns OFF.

This introduces **hysteresis**, preventing relay chatter near the 
threshold.

Link to Video: https://youtu.be/pAPqDm5CAdE

---

## 🧾 Sample Output

Temperature: 29.35°C
Fan OFF
Temperature: 30.12°C
Fan ON

~
---

## 🛣 Future Roadmap

- ✅ Phase 1: Temperature sensor → Fan control (done)
- 🔜 Phase 2: Data logging (CSV) + basic dashboard (Flask or Dash)
- 🔜 Phase 3: Pressure map system with adjustable torque
- 🔜 Phase 4: Conveyor + camera + classification logic (Good/NG detection)
- 🔜 Phase 5: Full automation demo kit

---

## 📷 Images (Coming Soon)

- Breadboard setup
- Relay/fan in action
- Terminal output screenshot

---

## 👤 Author

**Kunal Dixit**  
Aspiring automation engineer building systems from the ground up  
[LinkedIn](https://linkedin.com/in/kudixit)

---

## 📄 License

MIT License — free to use, share, and modify



