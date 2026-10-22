from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import time
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
rtc_0 = unit.get(unit.RTC8563, unit.PORTA)








rtc_0.set_date_time(37, 1, 1, 1, 0, 0, 0)
while True:
  print((str('hours:') + str((rtc_0.get_date_time(2)))))
  print((str('minutes:') + str((rtc_0.get_date_time(1)))))
  print((str('seconds:') + str((rtc_0.get_date_time(0)))))
  wait(1)
  wait_ms(2)