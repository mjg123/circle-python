import time

from adafruit_circuitplayground.express import cpx

# You have to call cpx.pixels.show() to make changes now!
cpx.pixels.auto_write = False

def light_up(pixs):
    # pass a list of pixels, I'll make them light up
    cpx.pixels.fill((0,0,0))
    for p in pixs:
        cpx.pixels[p] = (0,8,64)
    cpx.pixels.show()

def show_right():
    light_up([0,1,2,3,4])

def show_left():
    light_up([5,6,7,8,9])

def show_top():
    light_up([3,4,5,6])

def show_bottom():
    light_up([0,1,8,9])

def show_none():
    light_up([])

while True:

    x,y,z = cpx.acceleration

    if x > 3:
        show_right()
    elif x < -3:
        show_left()

    elif y > 3:
        show_top()
    elif y < -3:
        show_bottom()

    else:
        show_none()

    time.sleep(0.1)
