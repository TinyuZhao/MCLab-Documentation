from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import ntptime
import time


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








ntp = ntptime.client(host='cn.pool.ntp.org', timezone=8)
while True:
  print(ntp.formatDatetime('-', ':'))
  print(ntp.getTimestamp())
  wait(1)
  wait_ms(2)