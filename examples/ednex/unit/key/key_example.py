from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
key_0 = unit.get(unit.KEY, unit.PORTB)








key_0.set_color(0xff0000, 50)
while True:
  print(key_0.get_switch_status())
  wait_ms(2)