import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
 
def distance():
    GPIO.output(18, True)
    time.sleep(0.000001)
    GPIO.output(18, False)
    start = time.time()
    stop = time.time()
    while GPIO.input(24) == 0:
        start = time.time()
    while GPIO.input(24) == 1:
        stop = time.time()
    distance = ((stop - start) * 17160)
    return distance

try:
    while True:
	entfernung_summe = 0
	for i in range (50):	
       	    messung = distance()
	    entfernung_summe = entfernung_summe + messung    
	    time.sleep(0.002)
	sensor1 = entfernung_summe/50
	print (sensor1)
except KeyboardInterrupt:
    GPIO.cleanup()
 
