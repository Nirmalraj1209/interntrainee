"""
Python File Handling (Automotive Focus)
What is File Handling?

Definition:
File handling means reading, writing, updating, and managing files using Python.

Python uses file handling to:

Read logs
Store reports
Save test results
Analyze vehicle data
Automate testing


Real-Time Automotive Example

In automotive companies, tools like:

CANoe
ECU Testing tools
HIL Testing systems
Vehicle Sensors
ADAS systems(ADAS = Advanced Driver Assistance Systems)

generate log files every second.


Example file:

vehicle_log.txt

RPM:3200 TEMP:90 SPEED:80 BRAKE:OFF
RPM:6500 TEMP:110 SPEED:130 BRAKE:OFF
RPM:2000 TEMP:70 SPEED:40 BRAKE:ON


Python reads this file automatically and checks:

High RPM?
Engine overheating?
Overspeed?
Brake issue?

This is called:

✅ Log Parsing
✅ Automation
✅ Automotive Data Analysis


Why File Handling Important in Automotive?


| Use Case           | Real-Time Purpose              |
| ------------------ | ------------------------------ |
| CAN Logs           | Read CAN messages              |
| ECU Testing        | Store test results             |
| HIL Testing        | Analyze hardware response      |
| Sensor Data        | Read temperature/speed         |
| Crash Logs         | Debug failures                 |
| Automation Testing | Generate reports automatically |


Basic File Handling Flow

Vehicle/ECU
     ↓
Log File Generated
     ↓
Python Reads File
     ↓
Analyze Data
     ↓
Generate Alert/Report

Python File Handling Syntax

1. Open File

f = open("vehicle_log.txt", "r")

Meaning:

| Part              | Meaning    |
| ----------------- | ---------- |
| open()            | Opens file |
| "vehicle_log.txt" | File name  |
| "r"               | Read mode  |


2. Read File

data = f.read()
print(data)

Output

RPM:3200 TEMP:90 SPEED:80 BRAKE:OFF
RPM:6500 TEMP:110 SPEED:130 BRAKE:OFF
RPM:2000 TEMP:70 SPEED:40 BRAKE:ON


3. Read Line by Line (Important in Automotive)

f = open("vehicle_log.txt", "r")

for line in f:
    print(line)


Real-Time Automotive Program

    Problem:

Detect:

High RPM
High Temperature
Overspeed

Python Program

f = open("vehicle_log.txt", "r")

for line in f:

    data = line.split()

    rpm = int(data[0].split(":")[1])
    temp = int(data[1].split(":")[1])
    speed = int(data[2].split(":")[1])
    brake = data[3].split(":")[1]

    print("----------------")

    print("RPM =", rpm)
    print("TEMP =", temp)
    print("SPEED =", speed)
    print("BRAKE =", brake)

    if rpm > 6000:
        print("High RPM Alert")

    if temp > 100:
        print("High Temperature Alert")

    if speed > 100 and brake == "OFF":
        print("Overspeed Warning")
Output


----------------
RPM = 3200
TEMP = 90
SPEED = 80
BRAKE = OFF

----------------
RPM = 6500
TEMP = 110
SPEED = 130
BRAKE = OFF

High RPM Alert
High Temperature Alert
Overspeed Warning

Explain Clearly
line.split()

data = line.split()

Converts:

RPM:6500 TEMP:110 SPEED:130 BRAKE:OFF

into:

['RPM:6500', 'TEMP:110', 'SPEED:130', 'BRAKE:OFF']

split(":")[1]

rpm = int(data[0].split(":")[1])

Step-by-step

'RPM:6500'.split(":")

Result:

['RPM', '6500']

[1] means second value:

6500

Important File Modes

| Mode  | Meaning         |
| ----- | --------------- |
| `"r"` | Read            |
| `"w"` | Write           |
| `"a"` | Append          |
| `"x"` | Create new file |


"""