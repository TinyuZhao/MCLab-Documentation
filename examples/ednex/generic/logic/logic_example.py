from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


i = None




import random




while True:
  i = random.randint(0, 255)
  if i > 127:
    print(i)
  wait_ms(2)
