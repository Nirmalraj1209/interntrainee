f = open("vehicle_log.txt", "r")
for line in f:
    data = line.split()
    rpm = int(data[2].split(":")[1])
    temp = int(data[3].split(":")[1])
    # print("RPM =", rpm, "TEMP =", temp)
    if rpm > 6000 or temp > 100:
        print("ALERT")
    else:
        print("NORMAL")
    print("-------------------")
    f.close()