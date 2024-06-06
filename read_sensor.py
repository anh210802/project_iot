import serial
import time

relay1_ON = [0, 6, 0, 0, 0, 255, 200, 91]
relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]

ser = serial.Serial("/dev/ttyUSB0", 115200)
print("OK")
count = 0

def setDevice1(state):
    if state == True:
        ser.write(bytearray(relay1_ON))
    else:
        ser.write(bytearray(relay1_OFF))

while True:
    count += 1
    if count == 10:
        setDevice1(True) 
    if count == 20:
        setDevice1(False)
        count = 0
    print(ser.read)
    time.sleep(1)
