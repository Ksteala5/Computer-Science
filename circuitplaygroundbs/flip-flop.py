#First impor board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time

# when program finishes, board enters a waiting state
while True:
    if cp.switch: 
        for i in range(0,5):
            cp.pixels[i] = (8,1,1)
        for i in range(5,10):
            cp.pixels[i] = (0,0,0)
    else:
        for i in range(5,10):
            cp.pixels[i] = (8,1,1)
        for i in range(0,5):
            cp.pixels[i] = (0,0,0)