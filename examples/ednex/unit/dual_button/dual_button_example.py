from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
dual_button_0 = unit.get(unit.DUAL_BUTTON, unit.PORTB)








while True:
  if dual_button_0.btnBlue.wasPressed():
    rgb.setColorAll(0x000099)
    print('Blue button pressed')
  elif dual_button_0.btnRed.wasPressed():
    rgb.setColorAll(0xcc0000)
    print('Red button pressed')
  wait_ms(2)