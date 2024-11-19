#First impor board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time


# when program finishes, board enters a waiting state
while True:
        x,y,z = cp.acceleration
        if x > 1:
            cp.pixels[1] = (0,3,0)
            cp.pixels[2] = (0,3,0)
            cp.pixels[3] = (0,3,0)
            cp.pixels[6] = (0,0,0)
            cp.pixels[7] = (0,0,0)
            cp.pixels[8] = (0,0,0)
        elif x < -1:
            cp.pixels[1] = (0,0,0)
            cp.pixels[2] = (0,0,0)
            cp.pixels[3] = (0,0,0)
            cp.pixels[6] = (0,3,0)
            cp.pixels[7] = (0,3,0)
            cp.pixels[8] = (0,3,0)