with open("vehicle_log.txt", "r") as f:

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