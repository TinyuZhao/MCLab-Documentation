from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
tof_0 = unit.get(unit.TOF, unit.PORTA)








while True:
  print(tof_0.distance)
  wait(0.1)
  wait_ms(2)