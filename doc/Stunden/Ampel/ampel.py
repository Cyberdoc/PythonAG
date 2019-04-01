from time import sleep
from RPi import GPIO

PKW_GRUEN = 5
PKW_GELB = 6
PKW_ROT = 13

FUSSGAENGER_GRUEN = 17
FUSSGAENGER_ROT = 27

class Ampel:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(PKW_GRUEN, GPIO.OUT)
        GPIO.setup(PKW_GELB, GPIO.OUT)
        GPIO.setup(PKW_ROT, GPIO.OUT)
        
        GPIO.setup(FUSSGAENGER_GRUEN, GPIO.OUT)
        GPIO.setup(FUSSGAENGER_ROT, GPIO.OUT)

        GPIO.output(PKW_GRUEN, GPIO.HIGH)
        GPIO.output(PKW_GELB, GPIO.LOW)
        GPIO.output(PKW_ROT, GPIO.LOW)
        
        GPIO.output(FUSSGAENGER_GRUEN, GPIO.LOW)
        GPIO.output(FUSSGAENGER_ROT, GPIO.HIGH)

    def fussgaengerGruen(self):
        GPIO.output(FUSSGAENGER_ROT, GPIO.LOW)
        GPIO.output(FUSSGAENGER_GRUEN, GPIO.HIGH)

    def fussgaengerRot(self):
        GPIO.output(FUSSGAENGER_GRUEN, GPIO.LOW)
        GPIO.output(FUSSGAENGER_ROT, GPIO.HIGH)

    def pkwGruen(self):
        GPIO.output(PKW_GELB, GPIO.HIGH)
        sleep(1)
        GPIO.output(PKW_GELB, GPIO.LOW)
        GPIO.output(PKW_ROT, GPIO.LOW)
        GPIO.output(PKW_GRUEN, GPIO.HIGH)

    def pkwRot(self):
        GPIO.output(PKW_GRUEN, GPIO.LOW)
        GPIO.output(PKW_GELB, GPIO.HIGH)
        sleep(1)
        GPIO.output(PKW_GELB, GPIO.LOW)
        GPIO.output(PKW_ROT, GPIO.HIGH)
