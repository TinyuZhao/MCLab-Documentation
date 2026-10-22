from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
pir_0 = unit.get(unit.PIR, unit.PORTB)








while True:
  if (pir_0.state) == 1:
    print('PIR Status: Detected')
  else:
    print('PIR Status: Not detected')
  wait_ms(2)