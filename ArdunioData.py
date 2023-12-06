

# Importing Libraries 
import serial 
import time 
arduinoData=serial.Serial('com5',115200)
time.sleep(1)

while True:
    while (arduinoData.inWaiting()==0):
        pass

    dataPacket=arduinoData.readline()
    print(dataPacket)







































