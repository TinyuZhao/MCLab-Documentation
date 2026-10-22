from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import module

import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




servo2 = module.get(module.SERVO2)





while True:
  for i in range(1, 5):
    servo2.position(i, 180)
    wait(1)
  wait(1)
  for i in range(1, 5):
    servo2.position(i, 0)
    wait(1)
  wait(1)
  wait_ms(2)
