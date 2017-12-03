import time

from adafruit_circuitplayground.express import cpx

# You have to call cpx.pixels.show() to make changes now!
cpx.pixels.auto_write = False

RED   = (128, 0,   0  )
GREEN = (0,   128, 0  )

while True:
    cpx.pixels.fill((0,0,0))

    if cpx.switch:
        col = RED
    else:
        col = GREEN


    for p in range(10):
        cpx.pixels[p] = col

    cpx.pixels.show()
    time.sleep(0.1)
