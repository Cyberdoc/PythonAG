# 1-Wire Temperatur Sensor

### 1-Wire aktivieren 

Console/Terminal starten

```bash
sudo lsmod
```  

Prüfen, ob in der Ausgabe die drei folgenden Zeilen vorhanden sind:

```bash
wire
w1_gpio
w1_therm
```

Wenn ```wire``` oder ```w1_gpio``` fehlen, muss 1-Wire über die Raspbian Config aktiviert werden.

Nach einem Neustart sollte 1-Wire aktiv sein (mit dem Befehl lsmod erneut prüfen). Wenn ```w1_therm``` noch fehlen sollte, dann folgendes ausführen:

```bash
sudo modprobe w1_therm
```

### 1-Wire Sensor auslesen

Nun sollte man im Verzeichnis ```/sys/bus/w1/devices/``` mit ```ls``` den Sensor sehen (Unterverzeichnis beginnt mit "28-").

Folgende Befehle ausführen, um die aktuellen Werte zu sehen:
```bash
cd /sys/bus/w1/devices/         # wechselt in das Verzeichnis der 1-Wire Geräte
cat 28-041670d740ff/w1_slave    # cat gibt den Inhalt der Datei w1_slave aus
```

Der Wert wir in Celsius ausgegeben, aber um den Faktor 1000 erhöht, z.B. ein Wert 23021, entspricht einer Temperatur von 23,021°C.