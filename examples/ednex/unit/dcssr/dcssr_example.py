from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
dcssr_0 = unit.get(unit.DC_SSR, unit.PORTA)








dcssr_0.init_mode(1)
dcssr_0.init_i2c_address(0x50)
dcssr_0.set_i2c_rgb_led(50, 50, 50)
print(dcssr_0.get_i2c_rgb_led())
while True:
  dcssr_0.set_i2c_ssr_state(1)
  print(dcssr_0.get_i2c_ssr_status())
  wait(1)
  dcssr_0.set_i2c_ssr_state(0)
  print(dcssr_0.get_i2c_ssr_status())
  wait(1)
  wait_ms(2)