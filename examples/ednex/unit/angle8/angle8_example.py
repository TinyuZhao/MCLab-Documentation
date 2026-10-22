from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
angle8_0 = unit.get(unit.ANGLE8, unit.PORTA)








angle8_0.init_i2c_address(0x43)
angle8_0.set_LED_RGB24_From(0, 8, 50, 50, 50, 50)
while True:
  print(angle8_0.get_button_status())
  print(angle8_0.get_adc12_raw(0))
  wait_ms(2)