import time

from adafruit_circuitplayground.express import cpx

cpx.pixels.fill((0,0,0))
cpx.pixels.show()

whichPixel=0
pixelColour=0

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos*3), int(255 - (pos*3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos*3)), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))


while True:
    cpx.pixels.fill((0,0,0))

    cpx.pixels[whichPixel] = wheel(pixelColour)
    cpx.pixels.show()

    whichPixel += 1
    if whichPixel == 10:
        whichPixel = 0

    pixelColour += 1
    if pixelColour == 256:
        pixelColour = 0

    time.sleep(0.05)
