from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








while True:
  power.setVibrationEnable(True)
  wait(1)
  power.setVibrationEnable(False)
  wait(1)
  wait_ms(2)