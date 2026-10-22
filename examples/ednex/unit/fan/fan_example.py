from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
fan_0 = unit.get(unit.FAN, unit.PORTB)








while True:
  fan_0.on(10)
  wait_ms(2)