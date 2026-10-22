from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
hall_0 = unit.get(unit.HALL, unit.PORTA)








while True:
  print((str('HALL Status: ') + str((hall_0.value()))))
  wait_ms(2)