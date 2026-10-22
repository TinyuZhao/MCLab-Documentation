from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
dlight_0 = unit.get(unit.DLIGHT, unit.PORTA)







def buttonA_wasPressed():
  global i2c0
  dlight_0.set_mode(0x10)
  print('Continous Mode 1')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global i2c0
  dlight_0.set_mode(0x20)
  print('One Shot Mode 1')
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global i2c0
  dlight_0.set_mode(0x07)
  print('Reset')
  pass
btnC.wasPressed(buttonC_wasPressed)


while True:
  print((str('lux value:') + str((dlight_0.get_lux()))))
  wait_ms(250)
  wait_ms(2)