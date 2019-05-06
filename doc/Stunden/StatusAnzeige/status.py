from RPi import GPIO

STATUS_17 = 17
STATUS_34 = 27
STATUS_50 = 5
STATUS_67 = 6
STATUS_85 = 13
STATUS_100 = 19

class Anzeige:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(STATUS_17, GPIO.OUT)
        GPIO.setup(STATUS_34, GPIO.OUT)
        GPIO.setup(STATUS_50, GPIO.OUT)
        GPIO.setup(STATUS_67, GPIO.OUT)
        GPIO.setup(STATUS_85, GPIO.OUT)
        GPIO.setup(STATUS_100, GPIO.OUT)

        self.reset()
        
    def reset(self):
        GPIO.output(STATUS_17, GPIO.LOW)
        GPIO.output(STATUS_34, GPIO.LOW)
        GPIO.output(STATUS_50, GPIO.LOW)
        GPIO.output(STATUS_67, GPIO.LOW)
        GPIO.output(STATUS_85, GPIO.LOW)
        GPIO.output(STATUS_100, GPIO.LOW)

    def status(self, wert):
        self.reset()
        
        if (wert == 100):
            GPIO.output(STATUS_100, GPIO.HIGH)

        if (wert >= 85):
            GPIO.output(STATUS_85, GPIO.HIGH)

        if (wert >= 67):
            GPIO.output(STATUS_67, GPIO.HIGH)

        if (wert >= 50):
            GPIO.output(STATUS_50, GPIO.HIGH)

        if (wert >= 34):
            GPIO.output(STATUS_34, GPIO.HIGH)

        if (wert >= 17):
            GPIO.output(STATUS_17, GPIO.HIGH)

