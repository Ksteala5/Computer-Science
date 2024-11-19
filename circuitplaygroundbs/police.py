from adafruit_circuitplayground import cp
import random  
import time
while True:
    for i in range (0,10,2): 
        cp.pixels.fill ((5,0,0))
        cp.play_tone(500, .5)
        time.sleep(0.25)
        cp.pixels.fill ((0,0,5))
        cp.play_tone(900, .5)
        time.sleep(0.25)