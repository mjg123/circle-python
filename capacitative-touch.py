import time

from adafruit_circuitplayground.express import cpx

# You have to call cpx.pixels.show() to make changes now!
cpx.pixels.auto_write = False

RED   = (128, 0,   0  )
GREEN = (0,   128, 0  )
BLUE  = (0,   0,   128)

YELLOW  = (128, 128, 0  )
CYAN    = (0,   128, 128)
MAGENTA = (128, 0,   128)

WHITE = (128, 128, 128)

while True:
    cpx.pixels.fill((0,0,0))

    # Capacitative touch doesn't work on A0

    if cpx.touch_A1:
        cpx.pixels[6] = RED

    if cpx.touch_A2:
        cpx.pixels[8] = GREEN

    if cpx.touch_A3:
        cpx.pixels[9] = BLUE

    if cpx.touch_A4:
        cpx.pixels[0] = YELLOW

    if cpx.touch_A5:
        cpx.pixels[1] = CYAN

    if cpx.touch_A6:
        cpx.pixels[3] = MAGENTA

    if cpx.touch_A7:
        cpx.pixels[4] = WHITE

    cpx.pixels.show()
    time.sleep(0.1)
