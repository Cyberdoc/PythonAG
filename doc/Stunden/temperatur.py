#!/usr/bin/python3
import time, sys
from status2 import AnzeigeKurz 

sensor = '/sys/bus/w1/devices/28-041670d740ff/w1_slave'
 
def readTempSensor(sensorName) :
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def readTempLines(sensorName) :
    lines = readTempSensor(sensorName)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readTempSensor(sensorName)
    temperaturStr = lines[1].find('t=')
    if temperaturStr != -1 :
        tempData = lines[1][temperaturStr+2:]
        tempCelsius = float(tempData) / 1000.0
        return tempCelsius
 
anzeige = AnzeigeKurz()
anzeige.define_range(23, 30)
try:
    while True :
        temp = readTempLines(sensor)
        anzeige.range_status(temp)
        print("Temperatur: " + str(temp) + " °C")
        time.sleep(10)
except KeyboardInterrupt:
    print('Temperaturmessung wird beendet')
except Exception as e:
    print(str(e))
    sys.exit(1)
finally:
    print('Programm wird beendet.')
    sys.exit(0)
