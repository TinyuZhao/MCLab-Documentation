from MakerAndCoder import *
from MakerAndCoder_ui import *
from uiflow import *
import unit


screen = MCScreen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
gps_0 = unit.get(unit.GPS, unit.PORTC)








while True:
  print(gps_0.gps_time)
  print(gps_0.latitude)
  print(gps_0.longitude)
  print(gps_0.pos_quality)
  wait_ms(2)