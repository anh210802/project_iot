import time
import serial

relay1_ON  = [1, 6, 0, 0, 0, 255, 201, 138]
relay1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

relay2_ON  = [2, 6, 0, 0, 0, 255, 201, 185]
relay2_OFF = [2, 6, 0, 0, 0, 0, 137, 249]

relay3_ON  = [3, 6, 0, 0, 0, 255, 200, 104]
relay3_OFF = [3, 6, 0, 0, 0, 0, 136, 40]

relay4_ON  = [4, 6, 0, 0, 0, 255, 201, 223]
relay4_OFF = [4, 6, 0, 0, 0, 0, 137, 159]

relay5_ON  = [5, 6, 0, 0, 0, 255, 200, 14]
relay5_OFF = [5, 6, 0, 0, 0, 0, 136, 78]

relay6_ON  = [6, 6, 0, 0, 0, 255, 200, 61]
relay6_OFF = [6, 6, 0, 0, 0, 0, 136, 125]

relay7_ON  = [7, 6, 0, 0, 0, 255, 201, 236]
relay7_OFF = [7, 6, 0, 0, 0, 0, 137, 172]

relay8_ON  = [8, 6, 0, 0, 0, 255, 201, 19]
relay8_OFF = [8, 6, 0, 0, 0, 0, 137, 83]

soil_temperature = [10, 3, 0, 6, 0, 1, 101, 112]
soil_moisture = [10, 3, 0, 7, 0, 1, 52, 176]

class ModbusRS485:
    def __init__(self, portName):
        self.ser = None
        self.portName = portName

    def getPort(self):
        return self.portName

    def openPort(self):
        try:
            self.portName = self.getPort()
            self.ser = serial.Serial(port=self.portName, baudrate=9600, timeout=1)
            print("Port opened successfully")
        except Exception as e:
            print(f"Cannot open the port: {e}")

    def modbus485_read(self):
        try:
            bytesToRead = self.ser.inWaiting()
            if bytesToRead > 0:
                out = self.ser.read(bytesToRead)
                data_array = [b for b in out]
                print("Received Data:", data_array)
                if len(data_array) >= 7:
                    array_size = len(data_array)
                    value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
                    return value
                else: 
                    return 400
            return 404
        except Exception as e:
            print(f"Error in reading data: {e}")
            return -1
        
    def modbus485_send(self, data):
        self.modbus485_clear_buffer()
        try:
            self.ser.write(serial.to_bytes(data))
        except Exception as e:
            print("Modbus485**", "Failed to write data:", e)
            return 0
        return
    
    def modbus485_clear_buffer(self):
        bytesToRead = self.ser.inWaiting()
        if bytesToRead > 0:
            out = self.ser.read(bytesToRead)
            print("Buffer: ", out)

    def setDevice1(self, state):
        try:
            if state == True:
                self.modbus485_send(relay1_ON)
            else:
                self.modbus485_send(relay1_OFF)
            time.sleep(0.5)
            value = self.modbus485_read()
            print(value)
            return value
        except Exception as e:
            print(f"Error in setting device state: {e}")

    def setDevice2(self, state):
        try:
            if state == True:
                self.modbus485_send(relay2_ON)
            else:
                self.modbus485_send(relay2_OFF)
            time.sleep(0.5)
            value = self.modbus485_read()
            print(value)
            return value
        except Exception as e:
            print(f"Error in setting device state: {e}")

    def setDevice3(self, state):
        try:
            if state == True:
                self.modbus485_send(relay3_ON)
            else:
                self.modbus485_send(relay3_OFF)
            time.sleep(0.5)
            value = self.modbus485_read()
            print(value)
            return value
        except Exception as e:
            print(f"Error in setting device state: {e}")

    def setDevice4(self, state):
        try:
            if state == True:
                self.modbus485_send(relay4_ON)
            else:
                self.modbus485_send(relay4_OFF)
            time.sleep(0.5)
            print(self.modbus485_read())
        except Exception as e:
            print(f"Error in setting device state: {e}")

    def setDevice5(self, state):
        try:
            if state == True:
                self.modbus485_send(relay5_ON)
            else:
                self.modbus485_send(relay5_OFF)
            time.sleep(0.5)
            print(self.modbus485_read())
        except Exception as e:
            print(f"Error in setting device state: {e}")

    def setDevice6(self, state):
        try:
            if state == True:
                self.modbus485_send(relay6_ON)
            else:
                self.modbus485_send(relay6_OFF)
            time.sleep(0.5)
            print(self.modbus485_read())
        except Exception as e:
            print(f"Error in setting device state: {e}")

    def setDevice7(self, state):
        try:
            if state == True:
                self.modbus485_send(relay7_ON)
            else:
                self.modbus485_send(relay7_OFF)
            time.sleep(0.5)
            print(self.modbus485_read())
        except Exception as e:
            print(f"Error in setting device state: {e}")

    def setDevice8(self, state):
        try:
            if state == True:
                self.modbus485_send(relay8_ON)
            else:
                self.modbus485_send(relay8_OFF)
            time.sleep(0.5)
            print(self.modbus485_read())
        except Exception as e:
            print(f"Error in setting device state: {e}")

    def readTempAndHumi(self):
        try:
            self.modbus485_send(soil_temperature)
            time.sleep(0.5)
            print(self.modbus485_read())
            self.modbus485_send(soil_moisture)
            time.sleep(0.5)
            print(self.modbus485_read())
        except Exception as e:
            print(f"Error in reading temperature and humidity: {e}")
