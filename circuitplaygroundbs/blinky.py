#First impor board specific tools
#EVERY PROJECT NEEDS THIS STATEMENT
from adafruit_circuitplayground import cp
import time

# when program finishes, board enters a waiting state
while True:
    cp.pixels.fill((0,0,0))
    time.sleep(.367)
    cp.pixels.fill((0,5,0))
    time.sleep(.367)
