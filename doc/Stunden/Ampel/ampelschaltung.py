from time import sleep
from RPi import GPIO
from ampel import Ampel

SCHALTER = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(SCHALTER, GPIO.IN)

ampel = Ampel()

def tasterGedrueckt(channel):
    print("Fussgänger möchte über die Straße")
    ampel.pkwRot()
    sleep(1)
    ampel.fussgaengerGruen()
    sleep(5)
    ampel.fussgaengerRot()
    sleep(1)
    ampel.pkwGruen()


GPIO.add_event_detect(SCHALTER, GPIO.RISING, callback=tasterGedrueckt)

                        
try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Programm beendet")
