from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import module

import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)




gps = module.get(module.GPS, (14, 13))



gps.set_time_zone(8)
while True:
  print((str('time:') + str((gps.gps_time))))
  print((str('data:') + str((gps.gps_date))))
  print((str('latitude:') + str((gps.latitude))))
  print((str('longitude:') + str((gps.longitude))))
  print((str('altitude:') + str((gps.altitude))))
  wait(1)
  wait_ms(2)