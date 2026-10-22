from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import module

import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




ain420 = module.get(module.AIN_420MA)



ain420.init_i2c_address(0x55)
while True:
  print(ain420.get_ain_current_value(1))
  wait(1)
  wait_ms(2)