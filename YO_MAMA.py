import board
import neopixel
from time import sleep
import random

pixels = neopixel.NeoPixel(board.D18, 48, brightness =1)

pixels.fill((0, 0, 0))


pixels[32] = (0, 255, 0)
pixels[31] = (0, 255, 0)
pixels[16] = (0, 255, 0)

sleep (0.1)

pixels.fill((0, 0, 0))

pixels[
