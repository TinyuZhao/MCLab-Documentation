from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
relay4_0 = unit.get(unit.RELAY4, unit.PORTA)


i = None
status = None







relay4_0.set_mode(1)
while True:
  status = not (relay4_0.get_relay_status(1))
  for i in range(5):
    relay4_0.set_relay_status(i, status)
  wait(1)
  wait_ms(2)
