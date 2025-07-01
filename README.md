# 🧠 Temperature-Based Fan Control using Raspberry Pi

This project is a beginner-to-intermediate home automation setup using  
a **Raspberry Pi**, **DS18B20 temperature sensor**, and a  
**relay-controlled fan**. It reads live temperature data, logs it, and  
controls the fan automatically or manually via a web dashboard.

---

## 🚀 Features

- 🔄 Reads temperature every 2 seconds from a DS18B20 sensor  
- 💾 Logs temperature data continuously to CSV for historical record  
- 📊 Live temperature visualization on a web dashboard using Dash  
- 🔌 Controls a fan via relay based on temperature thresholds  
- 🔘 Manual fan control from the dashboard with ON/OFF button  
- 💻 Written entirely in Python, runs directly on Raspberry Pi  
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

1. The DS18B20 sensor communicates with the Pi via the 1-Wire interface.  
2. Temperature is read every 2 seconds and logged to a CSV file for record-keeping.  
3. A Dash-powered web dashboard visualizes the live temperature data and shows the current fan status.  
4. When temperature ≥ 30°C, the relay activates, turning the fan ON.  
5. When temperature ≤ 28°C, the relay deactivates, turning the fan OFF — this hysteresis avoids relay chatter near thresholds.  
6. The dashboard also features a manual ON/OFF button to override automatic control.  

[Watch the demo video here](https://youtu.be/pAPqDm5CAdE)

---

## 🧾 Sample Output (Terminal & Dashboard)

```
Temperature: 29.35°C  
Fan OFF  
Temperature: 30.12°C  
Fan ON  
```

Dashboard shows a live updating graph and buttons for fan control.

---

## 🛣 Future Roadmap

- ✅ Phase 1: Temperature sensor → Fan control (completed)  
- ✅ Phase 2: Data logging, live visualization & manual fan control dashboard (completed)  
- 🔜 Phase 3: Pressure mapping system with adjustable torque  
- 🔜 Phase 4: Conveyor + camera + automated classification (Good/NG detection)  
- 🔜 Phase 5: Full automation demo kit for presentations & client demos  

---

## 📷 Images & Media (Coming Soon)

- Breadboard wiring & setup photos  
- Relay and fan in action video clips  
- Dashboard screenshots  

---

## 👤 Author

**Kunal Dixit**  
Aspiring automation engineer building smart systems from scratch  
[LinkedIn](https://linkedin.com/in/kudixit)

---

## 📄 License

MIT License — free to use, share, and modify
