from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
neopixel_0 = unit.get(unit.NEOPIXEL, unit.PORTB, 37)


R = None
G = None
B = None
i = None




import random




while True:
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)
  for i in range(1, 31):
    neopixel_0.setColorFrom(1,i,(R << 16) | (G << 8) | B)
  wait_ms(500)
  for i in range(1, 31):
    neopixel_0.setColorFrom(1, i, 0x000000)
  wait_ms(500)
  wait_ms(2)
