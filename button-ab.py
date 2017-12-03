import time

from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a or cpx.button_b:
        cpx.pixels.fill((0, 128, 0))
    else:
        cpx.pixels.fill((128, 0, 64))
    time.sleep(0.1)
