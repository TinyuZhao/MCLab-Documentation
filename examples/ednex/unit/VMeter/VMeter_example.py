from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
VMeter_0 = unit.get(unit.VMETER, unit.PORTA)








while True:
  print((str('Voltage: ') + str(((str((VMeter_0.voltage())) + str(' mV'))))))
  wait(0.3)
  wait_ms(2)