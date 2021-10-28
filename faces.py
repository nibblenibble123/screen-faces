import board
import neopixel
from time import sleep
import random
from gpiozero import Button
faceButton = Button(2)
textButton = Button(7)

pixels = neopixel.NeoPixel(board.D18, 48, brightness =1)
pixels.fill((0, 0, 0))
sleep(2)
pixels.fill((255, 0, 0))
pixels.show()
pixels.fill((0, 0, 0))
pixels.show()
sleep(2)

#smile face

pixels[14] = (0, 255, 0)
pixels[2] = (0, 255, 0)
pixels[3] = (0, 255, 0)
pixels[4] = (0, 255, 0)
pixels[5] = (0, 255, 0)
pixels[9] = (0, 255, 0)
pixels[34] = (0, 255, 0)
pixels[29] = (0, 255, 0)
pixels[26] = (0, 255, 0)
pixels[37] = (0, 255, 0)

pixels.show()
sleep(2)
pixels.fill((0, 0, 0))

#no emotion

pixels[14] = (0, 255, 0)
pixels[13] = (0, 255, 0)
pixels[12] = (0, 255, 0)
pixels[11] = (0, 255, 0)
pixels[10] = (0, 255, 0)
pixels[9] = (0, 255, 0)
pixels[34] = (0, 255, 0)
pixels[29] = (0, 255, 0)
pixels[26] = (0, 255, 0)
pixels[37] = (0, 255, 0)

pixels.show()
sleep(2)
pixels.fill((0, 0, 0))

#frown 

pixels[6] = (0, 255, 0)
pixels[1] = (0, 255, 0)
pixels[13] = (0, 255, 0)
pixels[12] = (0, 255, 0)
pixels[11] = (0, 255, 0)
pixels[10] = (0, 255, 0)
pixels[34] = (0, 255, 0)
pixels[29] = (0, 255, 0)
pixels[26] = (0, 255, 0)
pixels[37] = (0, 255, 0)

while True:
  int joe = random.randrange(1, 300)
  if joe == 30
    pixels[34] = (0, 0, 0)
    pixels[30] = (0, 255, 0)
    sleep(2)
    pixels[30] = (0, 0, 0)
    pixels[34] = (0, 255, 0)
  
