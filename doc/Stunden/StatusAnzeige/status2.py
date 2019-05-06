from RPi import GPIO

STATUS_LIST = [(17,17), (34,27), (50,5), (67,6), (85,13), (99,19)]

class AnzeigeKurz:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        for wert, pin in STATUS_LIST:
            GPIO.setup(pin, GPIO.OUT)
            
        self.reset()
        
    def reset(self):
        for wert, pin in STATUS_LIST:
            GPIO.output(pin, GPIO.LOW)
            
    def status(self, anzeige_wert):
        self.reset()
        
        for wert, pin in STATUS_LIST:
            if (anzeige_wert >= wert):
                GPIO.output(pin, GPIO.HIGH)

