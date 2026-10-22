from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)








rtc.settime('ntp', host='cn.pool.ntp.org', tzone=8)
while True:
  print(rtc.printRTCtime())
  wait_ms(2)