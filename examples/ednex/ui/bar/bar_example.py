from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)






bar0 = MCBar(x=115, y=115, w=70, h=12, min=0, max=100, bg_c=0xa0a0a0, color=0x08A2B0, parent=None)

import random



while True:
  bar0.set_value(random.randint(0, 100))
  print(bar0.get_value())
  wait(1)
  wait_ms(2)