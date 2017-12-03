import time

from adafruit_circuitplayground.express import cpx

# You have to call cpx.pixels.show() to make changes now!
cpx.pixels.auto_write = False

RED   = (128, 0,   0  )
GREEN = (0,   128, 0  )
BLUE  = (0,   0,   128)

start_temp = cpx.temperature

while True:
    cpx.pixels.fill((0,0,0))

    ## BREATHE ON IT!!!

    print(cpx.temperature - start_temp)

    redness = int((cpx.temperature - start_temp) * 100)
    if redness < 0:
        redness = 0
    if redness > 255:
        redness = 255

    cpx.pixels.fill((redness, 0, 0))

    cpx.pixels.show()
    time.sleep(0.1)
