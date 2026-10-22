from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
env3_0 = unit.get(unit.ENV3, unit.PORTA)


while True:
  print(env3_0.pressure)
  print(env3_0.temperature)
  print(env3_0.humidity)
  wait_ms(10)
  wait_ms(2)
