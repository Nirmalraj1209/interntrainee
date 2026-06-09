"""
Python Basics
↓
File Handling
↓
Excel Automation
↓
Log Parsing
↓
API Automation
↓
Testing Automation
↓
Automotive Automation


1. Python Basics

What is it?

Python is a high-level programming language used to automate tasks.

Real-Time Example

Instead of manually calculating 100 employee salaries:


salary = 25000
bonus = 5000

total = salary + bonus

print(total)

Where used in company?
Employee tools
Data processing
Automation scripts
Backend systems
Testing

Important concepts

| Concept   | Example            |
| --------- | ------------------ |
| Variable  | `name = "Nirmal"`  |
| Condition | `if speed > 100:`  |
| Loop      | `for row in data:` |
| Function  | `def calculate():` |


2. File Handling

What is it?

Python reads files automatically.

Real-Time Example

Suppose vehicle logs are stored in:
RPM:6500 TEMP:105 SPEED:120

Python reads line by line.

with open("vehicle_log.txt", "r") as f:
    lines = f.readlines()

print(lines)

Real company usage

| Industry   | Usage                  |
| ---------- | ---------------------- |
| Automotive | Read CAN logs          |
| Banking    | Read transaction files |
| Testing    | Read test reports      |
| IT Support | Read server logs       |

Quick Comparison Table

| Mode  | Purpose         | File Exists?       | Old Data  |
| ----- | --------------- | ------------------ | --------- |
| `"r"` | Read            | Must exist         | Safe      |
| `"w"` | Write           | Creates if missing | Deleted   |
| `"a"` | Append          | Creates if missing | Preserved |
| `"x"` | Create new only | Error if exists    | Safe      |



3. Excel Automation

What is it?

Python automatically creates or edits Excel files.

Library mostly used:

openpyxl
pandas

Real-Time Example

Instead of manually sorting employee names in Excel:

from openpyxl import Workbook

Python automatically:

Reads data
Sorts data
Creates Excel
Applies formatting

Real company usage

| Usage           | Example               |
| --------------- | --------------------- |
| HR Reports      | Employee list         |
| Testing Reports | Failed test cases     |
| Finance         | Invoice automation    |
| Automotive      | ECU report generation |

4. Log Parsing

What is log parsing?

Reading machine/system logs automatically.

Real-Time Automotive Example

Vehicle generates:

RPM:7000 TEMP:110 SPEED:130 BRAKE:OFF

if rpm > 6000:
    print("High RPM Alert")

Real company usage

| Area       | Example          |
| ---------- | ---------------- |
| Automotive | ECU monitoring   |
| Servers    | Error detection  |
| Testing    | Failure analysis |
| Networking | Packet logs      |

5. API Automation
What is API?

Systems communicate using APIs.

Frontend → Backend → Database

Real-Time Example

Furniture website login:

React Frontend
↓
Spring Boot API
↓
MySQL

Python can test APIs automatically.


import requests

response = requests.get("http://localhost:8080/api/products")

print(response.json())


Real company usage

| Usage      | Example           |
| ---------- | ----------------- |
| Testing    | API validation    |
| Automation | Trigger services  |
| DevOps     | Server monitoring |


6. Testing Automation

What is it?

Instead of manually clicking buttons, Python tests automatically.


Real-Time Example

Check login automatically:

if username == "admin":
    print("Login Passed")

Tools used

| Tool     | Purpose        |
| -------- | -------------- |
| Selenium | Web automation |
| Pytest   | Testing        |
| Requests | API testing    |


8. Libraries You Should Learn

| Library      | Purpose          |
| ------------ | ---------------- |
| `openpyxl`   | Excel automation |
| `pandas`     | Data processing  |
| `requests`   | API automation   |
| `matplotlib` | Graphs           |
| `os`         | File operations  |
| `json`       | API data         |
| `re`         | Pattern matching |
| `pytest`     | Testing          |

"""