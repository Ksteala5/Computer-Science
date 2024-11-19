#First import board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time  
count = 0
while True:
    if cp.button_a:
        count += 1
        while cp.button_a:
            pass
        cp.pixels[-1+count] = (1,1,1)
    if cp.button_b:
        count -= 1
        while cp.button_b:
            pass
        cp.pixels[0+count] = (0,0,0)
    if count <= -1:
        count = 0
    if count > 9:
        count = 9