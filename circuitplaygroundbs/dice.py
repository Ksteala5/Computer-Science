#First impor board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import random  
import time
while True:
    #button press
    #randint 0-10
    if cp.button_a:
        number = random.randint(0,10)
        cp.pixels.fill((0,0,0))
        for i in range(0,number):
            cp.pixels[i]=(8,1,8)
            

    if cp.button_b:
        cp.pixels.fill((0,0,0))
        time.sleep(.115)
        cp.pixels.fill((0,1,0))
        time.sleep(.115)
        cp.pixels.fill((0,0,0))