from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
rgb_0 = unit.get(unit.RGB, unit.PORTB)








while True:
  rgb_0.setColor(1, 0xff0000)
  rgb_0.setColor(2, 0x33ff33)
  rgb_0.setColor(3, 0x3366ff)
  wait(0.1)
  wait_ms(2)