  
### Aufgabe 1
Bringt eure LED zum leuchten

```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)
```

### Aufgabe 2
Erweitert das Programm, dass die LED nach 5 Sekunden wieder ausgeschaltet wird.

### Aufgabe 3
Die LED soll eingeschaltet werden, nach 3 Sekunden aus und nach weiteren 3 Sekunden wieder an, bis das Programm manuell beendet wird. Das ein und ausschalten soll dabei mittels eigener Funktionen erfolgen, die der Aufgabe entsprechende Namen haben (z.B. `ledEinschalten`)

### Aufgabe 4
Der Benutzer gibt über eine Benutzereingabe an, wie oft der Vorgang durchgeführt werden soll. Der Benutzer-Wert darf nur zwischen 1 und 10 liegen. Ist der Wert nicht in dem Bereich, wird der Benutzer solange gefragt bis der Wert in diesem Bereich liegt.
