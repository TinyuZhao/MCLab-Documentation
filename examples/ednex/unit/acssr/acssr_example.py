from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
acssr_0 = unit.get(unit.AC_SSR, unit.PORTA)








acssr_0.init_i2c_address(0x50)
acssr_0.set_i2c_rgb_led(50, 50, 50)
print(acssr_0.get_i2c_rgb_led())
while True:
  acssr_0.set_i2c_ssr_state(1)
  print(acssr_0.get_i2c_ssr_status())
  wait(1)
  acssr_0.set_i2c_ssr_state(0)
  print(acssr_0.get_i2c_ssr_status())
  wait(1)
  wait_ms(2)