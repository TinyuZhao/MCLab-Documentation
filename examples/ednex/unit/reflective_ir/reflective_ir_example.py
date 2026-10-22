from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
reflective_ir_0 = unit.get(unit.REFLECTIVE_IR, unit.PORTB)








while True:
  print(reflective_ir_0.get_analog_output())
  print(reflective_ir_0.get_digital_output())
  wait(1)
  wait_ms(2)