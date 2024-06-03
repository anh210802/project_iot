print("Sensors and Actuators")

import time
import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort
    # return "/dev/ttyUSB1"

portName = "/dev/ttyUSB0"
print(portName)



try:
    ser = serial.Serial(port=portName, baudrate=115200)
    print("Open successfully")
except:
    print("Can not open the port")

relay1_ON  = [0, 6, 0, 0, 0, 255, 200, 91]
relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]

relay2_ON  = [15, 6, 0, 0, 0, 255, 200, 164]
relay2_OFF = [15, 6, 0, 0, 0, 0, 136, 228]

def setDevice1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)
    time.sleep(1)
    print("device1: " + serial_read_data(ser))

def setDevice2(state):
    if state == True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)
    time.sleep(1)
    print("device2: " + serial_read_data(ser))

def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    out = ser.read(bytesToRead)
    return out

# soil_temperature =[1, 3, 0, 6, 0, 1, 100, 11]
# def readTemperature():
#     serial_read_data(ser)
#     ser.write(soil_temperature)
#     time.sleep(1)
#     return serial_read_data(ser)

# soil_moisture = [1, 3, 0, 7, 0, 1, 53, 203]
# def readMoisture():
#     serial_read_data(ser)
#     ser.write(soil_moisture)
#     time.sleep(1)
#     return serial_read_data(ser)

counter = 0
while True:
    if counter >= 5:
        setDevice1(True)
        setDevice2(False)
        print("Relay1 : ON")
        print("Relay2 : OFF")
    else:
        setDevice1(False)
        setDevice2(True)
        print("Relay1 : OFF")
        print("Relay2 : ON")
    if counter == 10:
        counter = 0
    counter += 1
    time.sleep(1)
