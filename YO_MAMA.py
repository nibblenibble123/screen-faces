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

pixels[33] = (0, 255, 0)
pixels[30] = (0, 255, 0)
pixels[17] = (0, 255, 0)
pixels[0] = (0, 255, 0)]
pixels[16] = (0, 255, 0)
pixels[15] = (0, 255, 0)

sleep (0.1)
pixels.fill((0, 0, 0))

pixels[32] = (0, 255, 0)
pixels[31] = (0, 255, 0)
pixels[16] = (0, 255, 0)
pixels[17] = (0, 255, 0)
pixels[14] = (0, 255, 0)
pixels[1] = (0, 255, 0)
pixels[34] = (0, 255, 0)
pixels[29] = (0, 255, 0)
pixels[18] = (0, 255, 0)

sleep (0.1)
pixels.fill((0, 0, 0))

pixels[35] = (0, 255, 0)
pixels[28] = (0, 255, 0)
pixels[19] = (0, 255, 0)
pixels[18] = (0, 255, 0)
pixels[13] = (0, 255, 0)
pixels[2] = (0, 255, 0)
pixels[33] = (0, 255, 0)
pixels[30] = (0, 255, 0)
pixels[17] = (0, 255, 0)

sleep (0.1)
pixels.fill((0, 0, 0))
