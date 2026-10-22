from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import module

import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




relay4 = module.get(module.RELAY4)





relay4_0 = relay4.init_i2c_address(0x26)
while True:
  relay4_0.set_all_relay_state(1)
  wait(1)
  for i in range(1, 5):
    relay4_0.set_relay_state(i, 1)
    wait(0.2)
  wait(1)
  wait_ms(2)
