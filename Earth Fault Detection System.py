# Earth-Fault-Detection-System
# Earth Fault Detection System

# Safe leakage current limit
limit = 30  # mA

# Get leakage current
leakage = float(input("Enter leakage current (mA): "))

# Earth fault detection
if leakage > limit:
    print("EARTH FAULT DETECTED!")
    print("Relay TRIPPED")
    print("Load DISCONNECTED")
else:
    print("SYSTEM NORMAL")
    print("Relay ON")
    print("Load CONNECTED")
