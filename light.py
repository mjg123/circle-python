import time

from adafruit_circuitplayground.express import cpx

# You have to call cpx.pixels.show() to make changes now!
cpx.pixels.auto_write = False

RED   = (128, 0,   0  )

while True:
    cpx.pixels.fill((0,0,0))

    ## COVER IT UP!!!

    if cpx.light < 5:
        cpx.pixels.fill(RED)

    cpx.pixels.show()
    time.sleep(0.1)
