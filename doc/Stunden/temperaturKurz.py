#!/usr/bin/python3
import time, sys

sensor = '/sys/bus/w1/devices/28-041670d740ff/w1_slave'
 
def readSensor() :
    f = open(sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def readTemperature() :
    lines = readSensor()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readSensor()
    temperaturStr = lines[1].find('t=')
    if temperaturStr != -1 :
        tempData = lines[1][temperaturStr+2:]
        tempValue = float(tempData) / 1000.0
        return tempValue
 
try:
    while True :
        temp = readTemperature()
        print("Temperatur: " + str(temp) + " °C")
        time.sleep(10)
except KeyboardInterrupt:
    print('Programm wird beendet')
finally:
    sys.exit(0)
