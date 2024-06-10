from Scheduler.scheduler import *
from Utilities.modbusRS485 import *
from Utilities.mqttClient import *
from PrivateTasks.private_handleDevice import *
from PrivateTasks.private_handleSchedules import *
import time
import threading



MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "btl_iot_server"
MQTT_PASSWORD = ""
MQTT_TOPIC_SUB = ["/feeds/V1", "/feeds/V2", "/feeds/V3", "/feeds/V4", "/feeds/V5", "/feeds/V6", 
                  "/feeds/V7", "/feeds/V8", "/feeds/V12", "/feeds/V13", "/feeds/V14"]

COM_PORT = "COM5"


ser = ModbusRS485(COM_PORT)
scheduler = Scheduler()
client_mqtt = MQTT(MQTT_SERVER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD, MQTT_TOPIC_SUB)
device = HandleDevice(client_mqtt, ser, scheduler)

ser.openPort()
scheduler.SCH_Init()
threadServer = threading.Thread(target=client_mqtt.start)
threadServer.start()

# scheduler.SCH_Add_Task(ser.readTempAndHumi, 1, 10000)
scheduler.SCH_Add_Task(device.start, 1, 1000)



while True:
    device.start()
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
