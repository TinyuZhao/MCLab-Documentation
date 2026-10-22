from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
RF433T_0 = unit.get(unit.RF433TX, unit.PORTB)








while True:
  RF433T_0.transmit([1, 2, 3], 1)
  wait(1)
  wait_ms(2)