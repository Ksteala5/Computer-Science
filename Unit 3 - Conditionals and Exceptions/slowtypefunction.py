# SLOW TYPEWRITER!!

import time
import sys

def typewrite(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 

text = "Hello, World!"
typewrite(text)