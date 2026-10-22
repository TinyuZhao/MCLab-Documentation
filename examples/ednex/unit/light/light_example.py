from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
light_0 = unit.get(unit.LIGHT, unit.PORTB)








while True:
  print(light_0.digitalValue)
  print(light_0.analogValue)
  wait(0.2)
  wait_ms(2)