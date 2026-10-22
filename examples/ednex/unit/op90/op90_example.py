from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
OP90_0 = unit.get(unit.OP, unit.PORTA)








while True:
  print(OP90_0.value())
  wait(1)
  wait_ms(2)