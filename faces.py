import board
import neopixel
from time import sleep
import random
from gpiozero import Button

faceValue = 0

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



while True:
  faceButton.wait_for_press()
  
  
  int joe = random.randrange(1, 300)
  if joe == 30
    pixels[34] = (0, 0, 0)
    pixels[30] = (0, 255, 0)
    sleep(2)
    pixels[30] = (0, 0, 0)
    pixels[34] = (0, 255, 0)
  
