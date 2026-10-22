from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
from easyIO import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








while True:
  print(analogRead(39))
  wait_ms(2)