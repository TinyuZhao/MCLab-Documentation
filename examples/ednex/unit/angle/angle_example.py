from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
angle_0 = unit.get(unit.ANGLE, unit.PORTB)








while True:
  print(angle_0.read())
  wait_ms(10)
  wait_ms(2)