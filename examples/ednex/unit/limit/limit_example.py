from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
limit_0 = unit.get(unit.LIMIT, unit.PORTB)








while True:
  print(limit_0.get_switch_status())
  wait_ms(2)