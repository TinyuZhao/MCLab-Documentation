from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
joystick_0 = unit.get(unit.JOYSTICK, unit.PORTA)








while True:
  print(joystick_0.X)
  print(joystick_0.Y)
  print(joystick_0.Press)
  wait(0.2)
  wait_ms(2)