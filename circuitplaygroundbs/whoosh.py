#First impor board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time

# when program finishes, board enters a waiting state
while True:
    if cp.button_a:
        for i in range(0,10):
            cp.pixels[i] = (255,255,255)
            time.sleep(.1)
            cp.pixels[i] = (0,0,0) 