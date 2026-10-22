from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
ssr_0 = unit.get(unit.SSR, unit.PORTA)







def buttonA_wasPressed():
  global i2c0
  ssr_0.ssr_control(1)
  print('ON')
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  global i2c0
  ssr_0.ssr_control(0)
  print('OFF')
  pass
btnC.wasPressed(buttonC_wasPressed)

