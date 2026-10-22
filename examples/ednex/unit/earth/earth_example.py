from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
earth_0 = unit.get(unit.EARTH, unit.PORTB)








while True:
  print(earth_0.analogValue)
  print(earth_0.digitalValue)
  wait(0.2)
  wait_ms(2)