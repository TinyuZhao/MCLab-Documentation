from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
ir_0 = unit.get(unit.IR_NEC, unit.PORTB)








while True:
  ir_0.txOn()
  if (ir_0.rxStatus()) == 0:
    print('Detected')
    wait(0.1)
  else:
    print('Not detected')
  wait_ms(2)