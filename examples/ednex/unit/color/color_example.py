from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
color_0 = unit.get(unit.COLOR, unit.PORTA)








while True:
  print((str('R:') + str(str((color_0.red)))))
  print((str('G:') + str(str((color_0.green)))))
  print((str('B:') + str(str((color_0.blue)))))
  wait_ms(2)