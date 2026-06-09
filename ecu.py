f = open("ecu_log.txt", "r")

for line in f:

    data = line.split()

    rpm = int(data[2].split(":")[1])
    temp = int(data[3].split(":")[1])
    fuel = int(data[4].split(":")[1])
    brake = data[5].split(":")[1]
    speed = int(data[1].split(":")[1])

    print( "RPM =", rpm, "TEMP =", temp, "FUEL =", fuel, "BRAKE =", brake, "SPEED =", speed)

    if rpm > 6000:
        print("High RPM Alert")
    if temp > 100:
        print("High Temperature Alert")

    if fuel < 20:
        print("Low Fuel Warning")

    if speed > 100 and brake == "OFF":
        print("Overspeed Warning")

    print("-------------------")

f.close()