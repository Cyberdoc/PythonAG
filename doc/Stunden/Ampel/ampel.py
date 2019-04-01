from time import sleep
from RPi import GPIO

PKW_GRUEN = 17
PKW_GELB = 18
PKW_ROT = 19

FUSSGAENGER_GRUEN = 20
FUSSGAENGER_ROT = 21

class Ampel:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(PKW_GRUEN, GPIO.OUT)
        GPIO.setup(PKW_GELB, GPIO.OUT)
        GPIO.setup(PKW_ROT, GPIO.OUT)
        GPIO.setup(FUSSGAENGER_GRUEN, GPIO.OUT)
        GPIO.setup(FUSSGAENGER_ROT, GPIO.OUT)

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
